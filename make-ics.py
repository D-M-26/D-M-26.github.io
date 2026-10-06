#!/usr/bin/env python3
"""يولّد ملف التقويم الثابت للدعوة (RFC 5545).

التاريخ والوقت كما كانا في الكود الأصلي دون تغيير:
الجمعة 2026-10-23، 20:00 حتى 23:30 بتوقيت الرياض.
"""
import datetime, io

FILENAME = "زواج-عبدالرحمن-عمر-الدايل.ics"
SUMMARY  = "زواج عبدالرحمن عمر الدايل بقاعة اليزيه بالرياض"
LOCATION = "قاعة اليزيه للاحتفالات بالرياض"
MAP_URL  = "https://maps.app.goo.gl/WRDp3uiGdHvainDf6?g_st=ic"
ALARM    = "تذكير بزواج عبدالرحمن عمر الدايل بقاعة اليزيه بالرياض"

def esc(text):
    # RFC 5545 §3.3.11 TEXT escaping
    bs = "\\"
    text = text.replace(bs, bs + bs)
    for ch in (";", ","):
        text = text.replace(ch, bs + ch)
    return text.replace("\n", bs + "n")

def fold(line):
    # RFC 5545 §3.1: max 75 octets per line, never splitting a UTF-8 character
    out, cur, size = [], "", 0
    for ch in line:
        n = len(ch.encode("utf-8"))
        limit = 75 if not out else 74          # continuation lines start with a space
        if size + n > limit:
            out.append(cur); cur, size = ch, n
        else:
            cur += ch; size += n
    out.append(cur)
    return "\r\n ".join(out)

stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%SZ")

lines = [
    "BEGIN:VCALENDAR",
    "VERSION:2.0",
    "PRODID:-//aldayel-almujalli//wedding-invite//AR",
    "CALSCALE:GREGORIAN",
    "METHOD:PUBLISH",
    "BEGIN:VTIMEZONE",
    "TZID:Asia/Riyadh",
    "BEGIN:STANDARD",
    "DTSTART:19700101T000000",
    "TZOFFSETFROM:+0300",
    "TZOFFSETTO:+0300",
    "TZNAME:+03",
    "END:STANDARD",
    "END:VTIMEZONE",
    "BEGIN:VEVENT",
    "UID:aldayel-almujalli-20261023@invite",
    "DTSTAMP:" + stamp,
    "DTSTART;TZID=Asia/Riyadh:20261023T200000",
    "DTEND;TZID=Asia/Riyadh:20261023T233000",
    "SUMMARY:" + esc(SUMMARY),
    "LOCATION:" + esc(LOCATION),
    "DESCRIPTION:" + esc(MAP_URL),
    "URL:" + MAP_URL,
    "BEGIN:VALARM",
    "ACTION:DISPLAY",
    "TRIGGER:-P1D",
    "DESCRIPTION:" + esc(ALARM),
    "END:VALARM",
    "END:VEVENT",
    "END:VCALENDAR",
]
body = "\r\n".join(fold(l) for l in lines) + "\r\n"
with io.open(FILENAME, "w", encoding="utf-8", newline="") as f:
    f.write(body)
print("wrote", FILENAME, len(body.encode("utf-8")), "bytes")
