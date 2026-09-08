"""Render template.html into index.html (EN) and vi/index.html (VI).

Copy lives here, in one place per language, so the two pages cannot drift.
Run after editing template.html, style.css, or the strings below:

    python3 build.py
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TEMPLATE = (ROOT / "template.html").read_text(encoding="utf-8")

APP_STORE_URL = "https://apps.apple.com/app/id6798649203"
PLAY_URL = "https://play.google.com/store/apps/details?id=com.ncstudio.daybox"

SVG = {
    "svg_smile": '<svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" aria-hidden="true"><circle cx="11" cy="12" r="1.3" fill="currentColor" stroke="none"/><circle cx="21" cy="12" r="1.3" fill="currentColor" stroke="none"/><path d="M9.5 19.5c1.6 2.3 3.8 3.5 6.5 3.5s4.9-1.2 6.5-3.5"/></svg>',
    "svg_check": '<svg viewBox="0 0 20 20" fill="currentColor" aria-hidden="true"><path d="M10 1.5a8.5 8.5 0 1 0 0 17 8.5 8.5 0 0 0 0-17zm-1.1 12.2L5.2 10l1.3-1.3 2.4 2.4 4.6-4.6 1.3 1.3-5.9 5.9z"/></svg>',
    "svg_plus": '<svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M10 4v12M4 10h12"/></svg>',
    "svg_flame": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3c1 3 4 4.5 4 8.5A4 4 0 0 1 8 12c0-1 .3-2 1-3 0 2 1 3 2 3 0-3 1-5 1-9z"/><path d="M12 21a6 6 0 0 0 6-6c0-2-1-3.5-2-5"/></svg>',
    "svg_chart": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><path d="M4 20V10M10 20V4M16 20v-8M22 20H2"/></svg>',
    "svg_grid": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><rect x="3" y="3" width="7" height="7" rx="1.5"/><rect x="14" y="3" width="7" height="7" rx="1.5"/><rect x="3" y="14" width="7" height="7" rx="1.5"/><rect x="14" y="14" width="7" height="7" rx="1.5"/></svg>',
    "svg_postcard": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M12 5v14M15 9h3M15 12h3"/></svg>',
}

STRINGS = {
    "en": {
        "lang": "en",
        "path": "/",
        "home": "/",
        "og_locale": "en_US",
        "alt_href": "/vi/",
        "alt_lang": "vi",
        "alt_label": "Tiếng Việt",
        "meta_title": "Boxlet — Your whole day, in one little box",
        "meta_description": "Boxlet is a visual micro-journal for iOS and Android. One board per day: photos, notes, checklists, mood, spending. Five seconds a moment, and a month you can look back on.",
        "nav_cta": "Get the app",
        "nav_aria": "Sections",
        "nav_why": "Why",
        "nav_cards": "Cards",
        "nav_lookback": "Look back",
        "hero_title": "Your whole day, in one little box",
        "hero_lead": "Boxlet is a visual micro-journal. Every day gets one board — drop in a photo, a note, a checklist, your mood, what you spent. Five seconds a moment, and a month you can actually look back on.",
        "store_apple_alt": "Download on the App Store",
        "store_play_alt": "Get it on Google Play",
        "fine_free": "Free",
        "fine_no_account": "No account needed",
        "fine_platforms": "iOS & Android",
        "alt_board": "A Boxlet board for one day: a photo card, checklist, mood, expense, note, link and weather laid out on a grid",
        "pillars_title": "Made for people who quit journaling",
        "pillars_lead": "Most diaries die on day three, in front of a blank page. Boxlet has no page — only cards, and each one takes seconds.",
        "p1_title": "Five seconds a moment",
        "p1_body": "Pick a card type, tap, done. If you can take a photo or tick a box, you can keep a journal.",
        "alt_picker": "The card picker sheet showing the card types: note, to-do, photo, mood, expense, link, weather, wake-up, bedtime, timer",
        "p2_title": "One app instead of four",
        "p2_body": "Notes, to-dos, spending and photos live on the same board, so the day is in one place — and so is the month.",
        "alt_expense": "Journey tab showing spending for the month with a daily chart and a category donut",
        "p3_title": "A few friends, not the internet",
        "p3_body": "Share a day with the people you'd actually tell. They can react and comment. No followers, no algorithm — and expenses are never shared.",
        "alt_feed": "Activity feed with a few friends' posts: a mood, a finished to-do list, a streak",
        "paper_title": "Ten kinds of paper",
        "paper_lead": "Every card type has its own faint tint. Up close each one reads like paper; from a distance a full board looks like a small collection of it.",
        "board_aria": "A sample day board built from Boxlet's card types",
        "alt_coffee": "Two cups of latte on a wooden table",
        "label_note": "Note",
        "label_todo": "Checklist",
        "label_mood": "Mood",
        "label_weather": "Weather",
        "label_expense": "Expense",
        "label_link": "Link",
        "label_wake": "Wake-up",
        "label_bed": "Bedtime",
        "label_timer": "Timer",
        "sample_note": "Walked without my phone for once",
        "sample_todo": "Run 20 minutes",
        "sample_mood": "Good",
        "sample_weather": "Sunny",
        "sample_expense": "$38",
        "sample_expense_meta": "2 items",
        "sample_link": "A slower kind of weekday",
        "sample_wake": "slept 8h 10m",
        "sample_bed": "lights out",
        "sample_timer": "Deep work",
        "add_card": "Add a card",
        "legend_note": "Note",
        "legend_todo": "Checklist",
        "legend_mood": "Mood",
        "legend_expense": "Expense",
        "legend_link": "Link",
        "legend_weather": "Weather",
        "legend_time": "Wake-up · Bedtime · Timer",
        "look_title": "See what the month actually felt like",
        "look_lead": "A day full of cards is a picture of how you lived it. Thirty of them are a picture of a month.",
        "look1_t": "Streaks",
        "look1_b": "Count the days you showed up — not how much you wrote.",
        "look2_t": "Journey",
        "look2_b": "Moods, finished tasks and spending charted over any period.",
        "look3_t": "History",
        "look3_b": "Every month laid out as a wall of boards you can scroll back through.",
        "look4_t": "Postcards",
        "look4_b": "Turn any day into an image and share it anywhere.",
        "alt_mood": "Journey tab with a month of mood faces on a calendar and a mood mix bar",
        "alt_postcard": "The postcard maker rendering a day's board as a shareable image",
        "closing_title": "Start today's box. It takes five seconds.",
        "pro_line": "Boxlet is free to use. Boxlet Pro is an optional subscription — monthly or yearly, with a 3-day free trial — billed through the App Store or Google Play.",
        "pro_terms": "Terms of use",
        "footer_aria": "Footer",
        "f_privacy": "Privacy",
        "f_terms": "Terms",
        "f_support": "Support",
        "f_devlog": "Build log",
        "f_delete": "Delete account",
    },
    "vi": {
        "lang": "vi",
        "path": "/vi/",
        "home": "/vi/",
        "og_locale": "vi_VN",
        "alt_href": "/",
        "alt_lang": "en",
        "alt_label": "English",
        "meta_title": "Boxlet — Cả ngày của bạn, trong một chiếc hộp",
        "meta_description": "Boxlet là nhật ký thị giác siêu nhẹ cho iOS và Android. Mỗi ngày một board: ảnh, ghi chú, checklist, cảm xúc, chi tiêu. Mỗi khoảnh khắc 5 giây, cuối tháng có thứ để nhìn lại.",
        "nav_cta": "Tải ứng dụng",
        "nav_aria": "Các phần",
        "nav_why": "Tại sao",
        "nav_cards": "Loại thẻ",
        "nav_lookback": "Nhìn lại",
        "hero_title": "Cả ngày của bạn, trong một chiếc hộp",
        "hero_lead": "Boxlet là nhật ký thị giác siêu nhẹ. Mỗi ngày một board — thả vào đó một tấm ảnh, một dòng ghi chú, một checklist, cảm xúc, khoản đã tiêu. Mỗi khoảnh khắc 5 giây, và cuối tháng có một thứ thật sự để nhìn lại.",
        "store_apple_alt": "Tải trên App Store",
        "store_play_alt": "Tải trên Google Play",
        "fine_free": "Miễn phí",
        "fine_no_account": "Không cần tài khoản",
        "fine_platforms": "iOS & Android",
        "alt_board": "Board một ngày trong Boxlet: thẻ ảnh, checklist, cảm xúc, chi tiêu, ghi chú, liên kết và thời tiết xếp trên lưới",
        "pillars_title": "Dành cho người từng bỏ nhật ký",
        "pillars_lead": "Phần lớn nhật ký chết ở ngày thứ ba, trước một trang giấy trắng. Boxlet không có trang — chỉ có thẻ, và mỗi thẻ mất vài giây.",
        "p1_title": "5 giây một khoảnh khắc",
        "p1_body": "Chọn loại thẻ, chạm, xong. Biết chụp ảnh hay tick một ô là biết viết nhật ký.",
        "alt_picker": "Bảng chọn loại thẻ: ghi chú, việc cần làm, ảnh, cảm xúc, chi tiêu, liên kết, thời tiết, thức dậy, đi ngủ, bấm giờ",
        "p2_title": "Một app thay bốn app",
        "p2_body": "Ghi chú, việc cần làm, chi tiêu và ảnh sống chung trên một board — nên cả ngày ở một chỗ, và cả tháng cũng vậy.",
        "alt_expense": "Tab Journey hiện chi tiêu trong tháng với biểu đồ theo ngày và vòng danh mục",
        "p3_title": "Vài người thân, không phải cả internet",
        "p3_body": "Chia sẻ một ngày cho những người bạn thật sự muốn kể. Họ thả cảm xúc và bình luận. Không follower, không thuật toán — và chi tiêu không bao giờ được chia sẻ.",
        "alt_feed": "Bảng tin hoạt động với vài bài của bạn bè: một cảm xúc, một checklist đã xong, một chuỗi ngày",
        "paper_title": "Mười loại giấy",
        "paper_lead": "Mỗi loại thẻ có một sắc giấy rất nhạt của riêng nó. Nhìn gần, thẻ nào cũng là giấy; nhìn xa, một board đầy đủ trông như một bộ sưu tập giấy màu nhỏ.",
        "board_aria": "Board một ngày mẫu dựng từ các loại thẻ của Boxlet",
        "alt_coffee": "Hai ly latte trên bàn gỗ",
        "label_note": "Ghi chú",
        "label_todo": "Checklist",
        "label_mood": "Cảm xúc",
        "label_weather": "Thời tiết",
        "label_expense": "Chi tiêu",
        "label_link": "Liên kết",
        "label_wake": "Thức dậy",
        "label_bed": "Đi ngủ",
        "label_timer": "Bấm giờ",
        "sample_note": "Lâu lắm mới đi bộ không nhìn điện thoại",
        "sample_todo": "Chạy 20 phút",
        "sample_mood": "Vui",
        "sample_weather": "Nắng",
        "sample_expense": "225.000₫",
        "sample_expense_meta": "2 khoản",
        "sample_link": "Một ngày thường chậm hơn",
        "sample_wake": "ngủ 8g 10p",
        "sample_bed": "tắt đèn",
        "sample_timer": "Làm việc sâu",
        "add_card": "Thêm thẻ",
        "legend_note": "Ghi chú",
        "legend_todo": "Checklist",
        "legend_mood": "Cảm xúc",
        "legend_expense": "Chi tiêu",
        "legend_link": "Liên kết",
        "legend_weather": "Thời tiết",
        "legend_time": "Thức dậy · Đi ngủ · Bấm giờ",
        "look_title": "Cuối tháng, thấy mình đã sống thế nào",
        "look_lead": "Một ngày đầy thẻ là bức tranh về cách bạn đã sống ngày đó. Ba mươi ngày là bức tranh về một tháng.",
        "look1_t": "Streak",
        "look1_b": "Đếm những ngày bạn có mặt — không phải bạn viết được bao nhiêu.",
        "look2_t": "Journey",
        "look2_b": "Cảm xúc, việc đã xong và chi tiêu vẽ thành biểu đồ theo bất kỳ kỳ nào.",
        "look3_t": "Lịch sử",
        "look3_b": "Mỗi tháng trải thành một bức tường board để cuộn ngược về.",
        "look4_t": "Bưu thiếp",
        "look4_b": "Biến bất kỳ ngày nào thành một tấm ảnh để chia sẻ đi bất cứ đâu.",
        "alt_mood": "Tab Journey với một tháng mặt cảm xúc trên lịch và thanh tỉ lệ cảm xúc",
        "alt_postcard": "Màn tạo bưu thiếp đang dựng board của một ngày thành ảnh để chia sẻ",
        "closing_title": "Mở chiếc hộp hôm nay. Chỉ mất 5 giây.",
        "pro_line": "Boxlet dùng miễn phí. Boxlet Pro là gói thuê bao tuỳ chọn — theo tháng hoặc theo năm, có 3 ngày dùng thử — thanh toán qua App Store hoặc Google Play.",
        "pro_terms": "Điều khoản sử dụng",
        "footer_aria": "Chân trang",
        "f_privacy": "Quyền riêng tư",
        "f_terms": "Điều khoản",
        "f_support": "Hỗ trợ",
        "f_devlog": "Nhật ký dựng app",
        "f_delete": "Xoá tài khoản",
    },
}


def store_buttons(s: dict) -> str:
    # Official badge artwork only — Apple and Google both require it, and a
    # custom button reads as "unofficial" next to every other app site.
    lang = s["lang"]
    apple = f"/assets/badges/appstore-{'vi-vn' if lang == 'vi' else 'en-us'}.svg"
    play = f"/assets/badges/play-{lang}.{'png' if lang == 'vi' else 'svg'}"
    return (
        f'<a class="badge" href="{APP_STORE_URL}"><img src="{apple}" width="160" height="54" alt="{s["store_apple_alt"]}"></a>\n      '
        f'<a class="badge" href="{PLAY_URL}"><img src="{play}" width="182" height="54" alt="{s["store_play_alt"]}"></a>'
    )


def render(lang: str) -> str:
    s = {**SVG, **STRINGS[lang]}
    s["store_buttons"] = store_buttons(s)
    out = TEMPLATE
    for key, value in s.items():
        out = out.replace("{{" + key + "}}", value)
    leftover = [line for line in out.splitlines() if "{{" in line]
    if leftover:
        raise SystemExit(f"[{lang}] unfilled placeholders:\n" + "\n".join(leftover))
    return out


if __name__ == "__main__":
    (ROOT / "index.html").write_text(render("en"), encoding="utf-8")
    (ROOT / "vi").mkdir(exist_ok=True)
    (ROOT / "vi" / "index.html").write_text(render("vi"), encoding="utf-8")
    print("built index.html, vi/index.html")
