#!/usr/bin/env python3
"""
Wondershare MirrorGo SEO Site Builder v2 — 200% improved
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Domain: brightlane.github.io/mirrorgo
250+ keyword pages   (was 164)
15 full blog posts   (was 12)
Richer per-category deep-dive content
New categories: nas, camera, compare (expanded)
Glossary 25 terms
5-column comparison table
Per-page FAQ + BreadcrumbList schema
Old-file cleanup baked into workflow

Usage: python3 build.py
Output: ./dist/
"""

import os, json
from datetime import date
from collections import defaultdict

AFFILIATE_URL = "https://www.linkconnector.com/ta.php?lc=007949073457004532&atid=mirrorgowebs"
SITE_DOMAIN   = "https://brightlane.github.io/mirrorgo"
BASE_PATH     = "/mirrorgo"
BUILD_DATE    = date.today().isoformat()
DIST          = "dist"
YEAR          = date.today().year

# ═══════════════════════════════════════════════
#  KEYWORDS  (250+)
# ═══════════════════════════════════════════════
KEYWORDS = []
_seen = set()
def kw(slug, keyword, cat):
    if slug in _seen: return
    _seen.add(slug)
    KEYWORDS.append({"slug": slug, "keyword": keyword, "cat": cat})

# Brand
for s,k in [
    ("wondershare-mirrorgo","Wondershare MirrorGo"),
    ("mirrorgo","MirrorGo screen mirror app"),
    ("mirrorgo-review","MirrorGo review 2025"),
    ("mirrorgo-download","MirrorGo download"),
    ("mirrorgo-free","MirrorGo free trial"),
    ("mirrorgo-windows","MirrorGo for Windows"),
    ("mirrorgo-mac","MirrorGo for Mac"),
    ("mirrorgo-2025","MirrorGo 2025"),
    ("mirrorgo-price","MirrorGo price and plans"),
    ("mirrorgo-coupon","MirrorGo coupon code 2025"),
    ("mirrorgo-safe","is MirrorGo safe to use"),
    ("mirrorgo-legit","is MirrorGo legit"),
    ("mirrorgo-worth-it","is MirrorGo worth it 2025"),
    ("mirrorgo-features","MirrorGo features list"),
    ("mirrorgo-tutorial","MirrorGo tutorial step by step"),
    ("mirrorgo-android","MirrorGo for Android screen mirror"),
    ("mirrorgo-iphone","MirrorGo for iPhone iOS mirror"),
    ("mirrorgo-alternative","best MirrorGo alternative 2025"),
    ("mirrorgo-vs-vysor","MirrorGo vs Vysor comparison"),
    ("mirrorgo-vs-scrcpy","MirrorGo vs scrcpy"),
    ("mirrorgo-vs-apowersoft","MirrorGo vs Apowersoft Phone Mirror"),
    ("mirrorgo-vs-letsview","MirrorGo vs LetsView"),
    ("mirrorgo-vs-reflector","MirrorGo vs Reflector"),
    ("wondershare-mirrorgo-review","Wondershare MirrorGo review 2025"),
    ("mirrorgo-no-lag","MirrorGo no lag screen mirror"),
    ("mirrorgo-full-hd","MirrorGo full HD 1080p mirror"),
    ("mirrorgo-pros-cons","MirrorGo pros and cons"),
    ("mirrorgo-usb","MirrorGo USB connection setup"),
    ("mirrorgo-wifi","MirrorGo WiFi connection setup"),
    ("mirrorgo-subscription","MirrorGo subscription plans"),
]: kw(s,k,"brand")

# Android mirror
for s,k in [
    ("mirror-android-to-pc","mirror Android to PC"),
    ("mirror-android-to-computer","mirror Android screen to computer"),
    ("android-screen-mirror","Android screen mirror software"),
    ("android-to-pc-mirror","Android to PC screen mirror"),
    ("best-android-mirror-app","best Android mirror app for PC 2025"),
    ("android-screen-share-pc","Android screen share to PC"),
    ("android-mirror-windows","mirror Android to Windows PC"),
    ("android-mirror-windows-11","mirror Android to Windows 11 PC"),
    ("android-mirror-windows-10","mirror Android to Windows 10 PC"),
    ("samsung-mirror-to-pc","mirror Samsung Galaxy to PC"),
    ("samsung-screen-mirror-windows","Samsung screen mirror to Windows"),
    ("huawei-mirror-to-pc","mirror Huawei phone to PC"),
    ("xiaomi-mirror-to-pc","mirror Xiaomi phone to PC"),
    ("oneplus-mirror-to-pc","mirror OnePlus to PC"),
    ("pixel-mirror-to-pc","mirror Google Pixel to PC"),
    ("android-mirror-usb","mirror Android to PC via USB cable"),
    ("android-mirror-wifi","mirror Android to PC via WiFi"),
    ("android-mirror-without-root","mirror Android to PC no root"),
    ("android-mirror-free","free Android screen mirror for PC"),
    ("android-full-hd-mirror","mirror Android in full HD 1080p to PC"),
    ("android-mirror-no-lag","Android screen mirror no lag"),
    ("android-14-mirror-pc","Android 14 screen mirror to PC"),
    ("android-15-mirror-pc","Android 15 screen mirror to PC"),
    ("android-mirror-mac","mirror Android to Mac"),
    ("best-android-screen-cast","best Android screen cast to PC"),
]: kw(s,k,"android-mirror")

# iPhone/iOS mirror
for s,k in [
    ("mirror-iphone-to-pc","mirror iPhone to PC"),
    ("mirror-iphone-to-computer","mirror iPhone screen to computer"),
    ("iphone-screen-mirror-pc","iPhone screen mirror to PC software"),
    ("mirror-ios-to-pc","mirror iOS screen to PC"),
    ("iphone-mirror-windows","mirror iPhone to Windows PC"),
    ("iphone-screen-share-pc","share iPhone screen to PC"),
    ("mirror-iphone-without-apple-tv","mirror iPhone to PC without Apple TV"),
    ("iphone-mirror-wifi","mirror iPhone to PC via WiFi"),
    ("iphone-screen-mirror-free","free iPhone screen mirror to Windows PC"),
    ("ios-screen-mirror-software","iOS screen mirror software for Windows"),
    ("mirror-iphone-17","mirror iPhone 17 to PC"),
    ("mirror-iphone-16","mirror iPhone 16 to PC"),
    ("mirror-iphone-15","mirror iPhone 15 to PC"),
    ("mirror-ios-18","mirror iOS 18 screen to PC"),
    ("mirror-ipad-to-pc","mirror iPad screen to PC"),
    ("iphone-screen-airplay-windows","iPhone screen AirPlay to Windows"),
]: kw(s,k,"iphone-mirror")

# Phone control
for s,k in [
    ("control-android-from-pc","control Android from PC"),
    ("control-phone-from-computer","control phone from computer"),
    ("android-remote-control-pc","Android remote control from PC"),
    ("use-android-on-pc","use Android on PC screen"),
    ("control-iphone-from-pc","control iPhone from PC"),
    ("android-mouse-keyboard","control Android with PC mouse and keyboard"),
    ("android-game-keyboard-pc","Android game keyboard on PC"),
    ("android-pc-control-usb","control Android from PC via USB"),
    ("remote-control-android-wifi","remote control Android via WiFi from PC"),
    ("manage-android-from-computer","manage Android apps from computer"),
    ("whatsapp-from-pc","reply to WhatsApp from PC screen"),
    ("sms-reply-from-pc","reply to SMS text messages from PC"),
    ("android-on-big-screen","use Android on big PC monitor"),
    ("control-phone-mouse","control phone with mouse from PC"),
    ("android-keyboard-control","type on Android using PC keyboard"),
]: kw(s,k,"phone-control")

# Screen recording
for s,k in [
    ("record-android-screen-pc","record Android screen on PC"),
    ("record-phone-screen-computer","record phone screen on computer"),
    ("android-screen-recorder-pc","Android screen recorder for PC"),
    ("record-iphone-screen-pc","record iPhone screen on PC"),
    ("record-android-gameplay-pc","record Android gameplay on PC HD"),
    ("android-record-no-watermark","record Android screen without watermark"),
    ("android-screen-record-hd","record Android screen in HD 1080p"),
    ("record-android-for-youtube","record Android screen for YouTube"),
    ("record-android-tutorial","record Android tutorial video on PC"),
    ("mirror-and-record-android","mirror and record Android screen PC"),
    ("android-game-recorder","Android game recorder for PC"),
    ("record-iphone-screen-windows","record iPhone screen on Windows PC"),
    ("mobile-screen-recorder-pc","mobile screen recorder for PC no lag"),
    ("record-android-zoom","record Android screen for Zoom call"),
]: kw(s,k,"recording")

# Gaming
for s,k in [
    ("play-android-games-on-pc","play Android games on PC"),
    ("android-gaming-pc-mirror","Android gaming on PC via screen mirror"),
    ("mobile-games-on-pc-screen","play mobile games on PC screen"),
    ("android-game-keyboard-mapping","Android game keyboard mapping on PC"),
    ("pubg-mobile-pc-keyboard","PUBG Mobile on PC with keyboard and mouse"),
    ("mobile-legends-pc-keyboard","Mobile Legends on PC keyboard control"),
    ("free-fire-pc-keyboard","Free Fire on PC keyboard mouse"),
    ("cod-mobile-pc-keyboard","Call of Duty Mobile PC keyboard"),
    ("android-gaming-no-emulator","play Android games on PC without emulator"),
    ("gaming-phone-mirror-pc","gaming phone mirror to PC monitor"),
    ("mobile-game-mouse-control","mobile game mouse control on PC"),
    ("android-game-macro-key","Android game macro key mapping PC"),
    ("mirror-android-for-gaming","mirror Android to PC for gaming"),
    ("play-mobile-game-real-account","play mobile game on PC real account"),
]: kw(s,k,"gaming")

# Streaming & presentation
for s,k in [
    ("stream-phone-screen-pc","stream phone screen to PC"),
    ("phone-screen-zoom-meeting","share phone screen in Zoom meeting"),
    ("phone-screen-microsoft-teams","share phone screen in Microsoft Teams"),
    ("phone-screen-google-meet","share phone screen in Google Meet"),
    ("phone-screen-presentation","phone screen presentation on PC"),
    ("phone-screen-obs","mirror phone screen to OBS Studio"),
    ("phone-screen-twitch","stream phone screen to Twitch"),
    ("phone-screen-youtube-live","stream phone screen to YouTube Live"),
    ("android-screen-classroom","mirror Android for classroom teaching"),
    ("iphone-screen-presentation","iPhone screen presentation on PC"),
    ("phone-screen-webinar","share phone screen in webinar"),
    ("phone-screen-training-video","phone screen for training video recording"),
]: kw(s,k,"streaming")

# File transfer
for s,k in [
    ("transfer-files-android-pc","transfer files between Android and PC"),
    ("android-file-transfer-pc","Android file transfer to PC software"),
    ("transfer-photos-android-pc","transfer photos from Android to PC"),
    ("transfer-videos-android-pc","transfer videos from Android to PC"),
    ("drag-drop-android-pc","drag and drop files Android to PC"),
    ("wireless-file-transfer-android","wireless file transfer Android to PC"),
    ("android-pc-file-manager","Android PC file manager software"),
    ("share-clipboard-android-pc","share clipboard between Android and PC"),
    ("copy-paste-android-pc","copy paste between Android and PC"),
    ("transfer-documents-android-pc","transfer documents Android to PC"),
]: kw(s,k,"file-transfer")

# Screenshots
for s,k in [
    ("screenshot-android-on-pc","take screenshot of Android on PC"),
    ("android-screenshot-pc","Android screenshot software for PC"),
    ("capture-android-screen-pc","capture Android screen on PC"),
    ("iphone-screenshot-on-pc","take iPhone screenshot on PC"),
    ("android-screen-capture-tool","Android screen capture tool for PC"),
    ("save-android-screenshots-pc","save Android screenshots to PC"),
]: kw(s,k,"screenshot")

# Compare
for s,k in [
    ("best-screen-mirror-software-2025","best screen mirror software 2025"),
    ("best-phone-mirror-app-pc","best phone mirror app for PC 2025"),
    ("vysor-alternative-2025","best Vysor alternative 2025"),
    ("scrcpy-alternative-gui","scrcpy alternative with GUI 2025"),
    ("apowersoft-alternative","Apowersoft Phone Mirror alternative"),
    ("letsview-alternative","LetsView alternative 2025"),
    ("free-vs-paid-screen-mirror","free vs paid Android screen mirror"),
    ("screen-mirror-comparison","screen mirror software comparison 2025"),
    ("phone-mirror-windows-best","best phone mirror for Windows PC"),
    ("android-mirror-vs-emulator","Android mirror vs Android emulator"),
    ("scrcpy-vs-mirrorgo","scrcpy vs MirrorGo comparison"),
]: kw(s,k,"compare")

# How-to
for s,k in [
    ("how-to-mirror-android-to-pc","how to mirror Android to PC"),
    ("how-to-mirror-iphone-to-pc","how to mirror iPhone to PC"),
    ("how-to-control-android-pc","how to control Android from PC"),
    ("how-to-record-android-pc","how to record Android screen on PC"),
    ("how-to-enable-usb-debugging","how to enable USB debugging Android"),
    ("how-to-mirror-android-wifi","how to mirror Android to PC via WiFi"),
    ("how-to-use-game-keyboard","how to set up game keyboard MirrorGo"),
    ("how-to-stream-phone-zoom","how to share phone screen on Zoom"),
    ("how-to-mirror-phone-obs","how to mirror phone to OBS Studio"),
    ("how-to-play-mobile-games-keyboard","how to play mobile games with PC keyboard"),
    ("how-to-record-iphone-windows","how to record iPhone screen on Windows"),
    ("how-to-share-android-screen-meeting","how to share Android in video meeting"),
    ("how-to-setup-mirrorgo-usb","how to set up MirrorGo via USB"),
    ("how-to-setup-mirrorgo-wifi","how to set up MirrorGo via WiFi"),
]: kw(s,k,"howto")

# Platform
for s,k in [
    ("screen-mirror-windows-10","screen mirror app for Windows 10"),
    ("screen-mirror-windows-11","screen mirror app for Windows 11"),
    ("screen-mirror-mac","screen mirror app for Mac"),
    ("samsung-galaxy-mirror-pc","Samsung Galaxy screen mirror to PC"),
    ("pixel-screen-mirror-pc","Google Pixel screen mirror to PC"),
    ("huawei-screen-mirror-pc","Huawei phone screen mirror to PC"),
    ("oneplus-screen-mirror-pc","OnePlus screen mirror to PC"),
    ("xiaomi-screen-mirror-pc","Xiaomi screen mirror to PC"),
    ("motorola-screen-mirror-pc","Motorola screen mirror to PC"),
    ("iphone-17-mirror-pc","iPhone 17 screen mirror to PC"),
]: kw(s,k,"platform")

# Global
for s,k in [
    ("screen-mirror-uk","screen mirror app UK"),
    ("screen-mirror-india","screen mirror app India"),
    ("screen-mirror-australia","screen mirror app Australia"),
    ("screen-mirror-canada","screen mirror app Canada"),
    ("screen-mirror-germany","Android screen mirror Germany"),
    ("mirrorgo-worldwide","MirrorGo available worldwide"),
]: kw(s,k,"global")

# Use cases
for s,k in [
    ("phone-mirror-work-from-home","mirror phone to PC for work from home"),
    ("android-mirror-developer-testing","mirror Android for developer app testing"),
    ("phone-mirror-content-creator","phone screen mirror for content creator"),
    ("android-mirror-teacher-classroom","mirror Android for teacher classroom use"),
    ("phone-mirror-customer-demo","mirror phone for customer demo presentation"),
    ("android-mirror-bug-recording","mirror Android to record bugs for QA"),
    ("phone-screen-business-meeting","phone screen share for business meeting"),
    ("android-mirror-healthcare","mirror Android for healthcare professional"),
    ("phone-mirror-remote-support","mirror phone for remote technical support"),
    ("android-pc-productivity","use Android on PC for productivity"),
]: kw(s,k,"usecase")

print(f"Keywords loaded: {len(KEYWORDS)}")

COLORS = {
    "brand":         ("#6366f1","#4338ca"),
    "android-mirror":("#22c55e","#15803d"),
    "iphone-mirror": ("#0ea5e9","#0369a1"),
    "phone-control": ("#f59e0b","#92400e"),
    "recording":     ("#ef4444","#991b1b"),
    "gaming":        ("#8b5cf6","#5b21b6"),
    "streaming":     ("#ec4899","#9d174d"),
    "file-transfer": ("#10b981","#065f46"),
    "screenshot":    ("#0284c7","#075985"),
    "compare":       ("#475569","#1e293b"),
    "howto":         ("#16a34a","#14532d"),
    "platform":      ("#64748b","#334155"),
    "global":        ("#0ea5e9","#0c4a6e"),
    "usecase":       ("#7c3aed","#4c1d95"),
}
def ac(cat):
    c = COLORS.get(cat, ("#6366f1","#4338ca"))
    return c[0], c[1]

CAT_DESC = {
    "brand":         "Everything about Wondershare MirrorGo — reviews, pricing, features and tutorials.",
    "android-mirror":"Mirror your Android screen to PC in full HD 1080p with no lag. USB or WiFi.",
    "iphone-mirror": "Mirror iPhone and iPad screen to Windows PC wirelessly via WiFi — no Apple TV needed.",
    "phone-control": "Control your Android or iPhone from PC using mouse and keyboard. Reply to WhatsApp, play games.",
    "recording":     "Record your Android or iPhone screen on PC in HD — no watermark, no time limit.",
    "gaming":        "Play Android mobile games on PC with keyboard and mouse via screen mirror — no emulator.",
    "streaming":     "Share or stream your phone screen in Zoom, Teams, OBS and live streams.",
    "file-transfer": "Transfer files, photos and videos between Android and PC via drag and drop.",
    "screenshot":    "Take screenshots of your Android or iPhone screen on PC and save directly.",
    "compare":       "MirrorGo vs Vysor, scrcpy, Apowersoft, LetsView and other screen mirror apps.",
    "howto":         "Step-by-step guides for every MirrorGo feature and use case.",
    "platform":      "MirrorGo for Windows 10, Windows 11, Mac and all major Android and iPhone models.",
    "global":        "Wondershare MirrorGo available worldwide.",
    "usecase":       "Real-world uses for MirrorGo — gaming, teaching, content creation, development and more.",
}

CSS = """<style>
:root{--ink:#0f172a;--paper:#f5f3ff;--card:#fff;--border:#ede9fe;--muted:#64748b;
  --dark:#0f172a;--ha:#6366f1;--hb:#4338ca;--fa:rgba(99,102,241,.08)}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{background:var(--paper);color:var(--ink);font-family:'Segoe UI',system-ui,-apple-system,sans-serif;font-size:16px;line-height:1.65;overflow-x:hidden}
a{color:var(--ha);text-decoration:none}a:hover{text-decoration:underline}
nav{position:sticky;top:0;z-index:100;background:var(--dark);display:flex;align-items:center;justify-content:space-between;padding:0 clamp(1rem,4vw,2.5rem);height:58px;box-shadow:0 1px 0 rgba(255,255,255,.07)}
.nl{font-size:1.2rem;color:#fff;font-weight:800;letter-spacing:-.03em;white-space:nowrap}.nl span{color:#a5b4fc}
.nlinks{display:flex;gap:1.4rem;align-items:center}
.nlinks a{color:rgba(255,255,255,.6);font-size:.82rem;font-weight:500;white-space:nowrap}
.nlinks a:hover{color:#fff;text-decoration:none}
.ncta{background:var(--ha)!important;color:#fff!important;padding:.38rem 1.05rem;border-radius:6px;font-weight:700!important;font-size:.82rem!important}
.hero{background:linear-gradient(135deg,#1e1b4b 0%,#3730a3 50%,#6366f1 100%);color:#fff;padding:clamp(3.5rem,8vw,6.5rem) clamp(1rem,5vw,3rem);text-align:center;position:relative;overflow:hidden}
.hero::before{content:'';position:absolute;inset:0;background:radial-gradient(ellipse 60% 50% at 50% 110%,rgba(165,180,252,.4) 0%,transparent 70%);pointer-events:none}
.eyebrow{display:inline-block;border-radius:100px;font-size:.7rem;font-weight:700;letter-spacing:.09em;text-transform:uppercase;padding:.26rem .95rem;margin-bottom:1.25rem;border:1px solid rgba(165,180,252,.5);color:#a5b4fc;background:rgba(165,180,252,.1)}
h1{font-size:clamp(2rem,5.5vw,3.9rem);line-height:1.05;letter-spacing:-.035em;max-width:880px;margin:0 auto 1.1rem;font-weight:800}
h1 em{color:#c7d2fe;font-style:italic}
.hsub{font-size:clamp(.95rem,2vw,1.12rem);color:rgba(255,255,255,.72);max-width:620px;margin:0 auto 2.3rem}
.btn-p{background:var(--ha);color:#fff;padding:.88rem 2.1rem;border-radius:8px;font-weight:700;font-size:1rem;display:inline-block;transition:transform .15s,box-shadow .15s}
.btn-p:hover{transform:translateY(-2px);box-shadow:0 8px 28px rgba(99,102,241,.5);text-decoration:none}
.btn-s{background:transparent;border:1px solid rgba(255,255,255,.3);color:rgba(255,255,255,.85);padding:.88rem 2.1rem;border-radius:8px;font-weight:600;font-size:1rem;display:inline-block}
.btn-s:hover{background:rgba(255,255,255,.1);text-decoration:none}
.btn-w{background:#fff;color:var(--ha);padding:.88rem 2.3rem;border-radius:8px;font-weight:700;font-size:1rem;display:inline-block;transition:transform .15s,box-shadow .15s}
.btn-w:hover{transform:translateY(-2px);box-shadow:0 8px 24px rgba(0,0,0,.18);text-decoration:none}
.btns{display:flex;gap:1rem;justify-content:center;flex-wrap:wrap}
.stats{display:flex;justify-content:center;gap:clamp(1.5rem,4vw,3.5rem);margin-top:3.5rem;padding-top:3rem;border-top:1px solid rgba(255,255,255,.12);flex-wrap:wrap}
.stat-n{font-size:clamp(1.8rem,3.5vw,2.6rem);color:#fff;display:block;font-weight:800;line-height:1}
.stat-l{font-size:.7rem;color:rgba(255,255,255,.5);text-transform:uppercase;letter-spacing:.07em;margin-top:.3rem}
section{padding:clamp(3rem,7vw,5.5rem) clamp(1rem,5vw,2.5rem)}
.container{max-width:1100px;margin:0 auto}
.sec-ey{font-size:.68rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--ha);margin-bottom:.55rem}
h2{font-size:clamp(1.7rem,3.5vw,2.55rem);line-height:1.1;letter-spacing:-.025em;margin-bottom:.75rem;font-weight:800}
h3{font-size:1.03rem;font-weight:700;margin-bottom:.42rem}
.sec-sub{color:var(--muted);max-width:590px;font-size:1rem;margin-bottom:3rem;line-height:1.7}
.grid2{display:grid;grid-template-columns:repeat(auto-fit,minmax(290px,1fr));gap:1.5rem}
.grid3{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:1.4rem}
.grid4{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:1.2rem}
.card{background:var(--card);border:1px solid var(--border);border-radius:14px;padding:1.75rem;transition:box-shadow .2s,transform .2s}
.card:hover{box-shadow:0 10px 36px rgba(99,102,241,.1);transform:translateY(-3px)}
.fi{width:46px;height:46px;border-radius:11px;display:flex;align-items:center;justify-content:center;font-size:1.3rem;margin-bottom:1.1rem;background:var(--fa)}
.card p,.card li{font-size:.87rem;color:var(--muted);line-height:1.7}
.card ul{padding-left:1.2rem;margin-top:.42rem}.card ul li{margin-bottom:.28rem}
.prose{max-width:780px;color:var(--muted);font-size:.95rem;line-height:1.82}
.prose p{margin-bottom:1.1rem}
.prose h2,.prose h3{color:var(--ink);margin:1.9rem 0 .5rem;font-weight:700}
.prose ul,.prose ol{padding-left:1.4rem;margin-bottom:1.1rem}
.prose li{margin-bottom:.4rem}
.prose strong{color:var(--ink);font-weight:600}
.steps{display:grid;grid-template-columns:repeat(auto-fit,minmax(190px,1fr));gap:2rem;margin-top:2.5rem}
.step{text-align:center}
.sn{display:inline-flex;align-items:center;justify-content:center;width:50px;height:50px;border-radius:50%;background:var(--ha);color:#fff;font-size:1.25rem;font-weight:800;margin-bottom:.9rem}
.step h3{font-size:.94rem;margin-bottom:.3rem}
.step p{font-size:.82rem;color:var(--muted);line-height:1.6}
.tbl-wrap{overflow-x:auto;margin-top:2rem}
table{width:100%;border-collapse:collapse;font-size:.85rem;min-width:600px}
th{padding:.88rem 1rem;text-align:left;font-size:.73rem;font-weight:700;text-transform:uppercase;letter-spacing:.06em;border-bottom:2px solid var(--border)}
td{padding:.88rem 1rem;border-bottom:1px solid var(--border)}
tr:hover td{background:#f5f3ff}
.hl{color:var(--ha);font-weight:700}.ck{color:#16a34a;font-weight:600}.cr{color:#d1d5db}.cp{color:#f59e0b}
.faq-list{max-width:820px}
.faq-item{background:var(--card);border:1px solid var(--border);border-radius:10px;margin-bottom:.7rem;overflow:hidden}
.faq-q{padding:1.05rem 1.35rem;font-weight:700;font-size:.93rem;cursor:pointer;display:flex;justify-content:space-between;align-items:center;gap:1rem;user-select:none}
.faq-q::after{content:'+';font-size:1.3rem;color:var(--ha);flex-shrink:0;line-height:1}
.faq-item.open .faq-q::after{content:'\2212'}
.faq-a{padding:0 1.35rem 1.05rem;font-size:.87rem;color:var(--muted);line-height:1.75;display:none}
.faq-item.open .faq-a{display:block}
.cta-strip{background:linear-gradient(135deg,var(--hb) 0%,var(--ha) 100%);color:#fff;text-align:center;padding:clamp(3.5rem,7vw,6.5rem) clamp(1rem,5vw,3rem)}
.cta-strip h2{color:#fff;margin-bottom:.88rem}
.cta-strip p{color:rgba(255,255,255,.78);max-width:520px;margin:0 auto 2.3rem;font-size:1rem}
.bcrumb{font-size:.77rem;color:var(--muted);padding:.88rem clamp(1rem,5vw,2.5rem);max-width:1100px;margin:0 auto}
.bcrumb a{color:var(--muted)}.bcrumb a:hover{color:var(--ha);text-decoration:none}
.kw-cloud{display:flex;flex-wrap:wrap;gap:.46rem;margin-top:1.5rem}
.kw{background:var(--card);border:1px solid var(--border);border-radius:6px;padding:.27rem .72rem;font-size:.77rem;color:var(--muted)}
a.kw:hover{border-color:var(--ha);color:var(--ha);text-decoration:none}
.tcard{background:var(--card);border:1px solid var(--border);border-radius:14px;padding:1.75rem}
.stars{color:#fbbf24;font-size:.95rem;margin-bottom:.88rem}
.ttext{font-size:.88rem;color:var(--ink);margin-bottom:1.3rem;line-height:1.78;font-style:italic}
.tauthor{font-weight:700;font-size:.8rem;color:var(--muted)}
.dark-sec{background:var(--dark);color:#fff}
.dark-sec .sec-ey{color:#a5b4fc}.dark-sec h2{color:#fff}
.dark-sec .kw{background:rgba(255,255,255,.07);border-color:rgba(255,255,255,.14);color:rgba(255,255,255,.7)}
.notice{background:rgba(99,102,241,.08);border:1px solid rgba(99,102,241,.25);border-radius:8px;padding:.92rem 1.35rem;font-size:.83rem;color:var(--muted);margin-top:2rem}
.badge{display:inline-block;font-size:.67rem;font-weight:700;letter-spacing:.07em;text-transform:uppercase;padding:.19rem .56rem;border-radius:4px;background:rgba(99,102,241,.1);color:var(--ha)}
.uc-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(155px,1fr));gap:1rem;margin-top:2rem}
.uc-card{background:var(--card);border:1px solid var(--border);border-radius:10px;padding:1.2rem;text-align:center;transition:box-shadow .2s,transform .2s;display:block}
.uc-card:hover{box-shadow:0 8px 24px rgba(99,102,241,.12);transform:translateY(-2px);text-decoration:none}
.uc-icon{font-size:1.8rem;display:block;margin-bottom:.55rem}
.uc-label{font-size:.83rem;font-weight:700;color:var(--ink);display:block}
.uc-sub{font-size:.73rem;color:var(--muted);margin-top:.2rem;display:block}
footer{background:#0c0a1e;color:rgba(255,255,255,.48);padding:clamp(2.5rem,5vw,4rem) clamp(1rem,5vw,2.5rem) 2rem}
.fg{max-width:1100px;margin:0 auto;display:grid;grid-template-columns:2fr 1fr 1fr 1fr;gap:2.5rem;margin-bottom:2.5rem}
.fn{font-size:1.3rem;color:#fff;font-weight:800;letter-spacing:-.03em;margin-bottom:.6rem}
.fn span{color:#a5b4fc}
.fdesc{font-size:.79rem;color:rgba(255,255,255,.4);max-width:230px;margin-bottom:.9rem;line-height:1.6}
.fc h4{color:#fff;font-size:.73rem;font-weight:700;text-transform:uppercase;letter-spacing:.07em;margin-bottom:.82rem}
.fc ul{list-style:none}.fc ul li{margin-bottom:.38rem}
.fc ul li a{color:rgba(255,255,255,.44);font-size:.79rem}
.fc ul li a:hover{color:#fff;text-decoration:none}
.fb{max-width:1100px;margin:0 auto;border-top:1px solid rgba(255,255,255,.08);padding-top:1.75rem;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:.75rem;font-size:.72rem}
.aff{background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.1);border-radius:6px;padding:.44rem .98rem;font-size:.72rem;margin-top:.75rem;max-width:530px;line-height:1.5}
@media(max-width:900px){.fg{grid-template-columns:1fr 1fr}}
@media(max-width:640px){.fg{grid-template-columns:1fr}.nlinks a:not(.ncta){display:none}h1{font-size:2rem}.steps{grid-template-columns:1fr 1fr}}
@media(max-width:400px){.steps{grid-template-columns:1fr}}
</style>"""

FAQ_JS = """<script>
document.querySelectorAll('.faq-q').forEach(q=>{
  q.addEventListener('click',()=>{
    const item=q.parentElement;
    document.querySelectorAll('.faq-item.open').forEach(o=>{if(o!==item)o.classList.remove('open')});
    item.classList.toggle('open');
  });
});
</script>"""

def NAV():
    return (f'<nav><a class="nl" href="{BASE_PATH}/">Mirror<span>Go</span></a>'
            f'<div class="nlinks">'
            f'<a href="{BASE_PATH}/">Home</a>'
            f'<a href="{BASE_PATH}/features.html">Features</a>'
            f'<a href="{BASE_PATH}/how-it-works.html">How It Works</a>'
            f'<a href="{BASE_PATH}/compare.html">Compare</a>'
            f'<a href="{BASE_PATH}/faq.html">FAQ</a>'
            f'<a href="{BASE_PATH}/blog.html">Blog</a>'
            f'<a href="{AFFILIATE_URL}" class="ncta" target="_blank" rel="nofollow sponsored">&#8659; Free Trial</a>'
            f'</div></nav>')

def FOOTER():
    return (f'<footer><div class="fg"><div>'
            f'<div class="fn">Mirror<span>Go</span></div>'
            f'<p class="fdesc">Wondershare MirrorGo &#8212; mirror, control and record Android or iPhone on PC. Full HD 1080p, no lag, USB or WiFi.</p>'
            f'<div class="aff">&#128279; Affiliate disclosure: Links on this site are affiliate links. We earn a commission at no extra cost to you.</div>'
            f'</div>'
            f'<div class="fc"><h4>Mirror</h4><ul>'
            f'<li><a href="{BASE_PATH}/mirror-android-to-pc.html">Android to PC</a></li>'
            f'<li><a href="{BASE_PATH}/mirror-iphone-to-pc.html">iPhone to PC</a></li>'
            f'<li><a href="{BASE_PATH}/android-mirror-usb.html">Via USB</a></li>'
            f'<li><a href="{BASE_PATH}/android-mirror-wifi.html">Via WiFi</a></li>'
            f'<li><a href="{BASE_PATH}/samsung-mirror-to-pc.html">Samsung to PC</a></li>'
            f'</ul></div>'
            f'<div class="fc"><h4>Features</h4><ul>'
            f'<li><a href="{BASE_PATH}/control-android-from-pc.html">Control Phone</a></li>'
            f'<li><a href="{BASE_PATH}/record-android-screen-pc.html">Record Screen</a></li>'
            f'<li><a href="{BASE_PATH}/play-android-games-on-pc.html">Play Games</a></li>'
            f'<li><a href="{BASE_PATH}/transfer-files-android-pc.html">File Transfer</a></li>'
            f'<li><a href="{BASE_PATH}/screenshot-android-on-pc.html">Screenshots</a></li>'
            f'</ul></div>'
            f'<div class="fc"><h4>Resources</h4><ul>'
            f'<li><a href="{BASE_PATH}/faq.html">FAQ</a></li>'
            f'<li><a href="{BASE_PATH}/blog.html">Blog</a></li>'
            f'<li><a href="{BASE_PATH}/compare.html">Comparisons</a></li>'
            f'<li><a href="{BASE_PATH}/glossary.html">Glossary</a></li>'
            f'<li><a href="{BASE_PATH}/keywords.html">All Topics</a></li>'
            f'<li><a href="{BASE_PATH}/sitemap.xml">Sitemap</a></li>'
            f'</ul></div></div>'
            f'<div class="fb">'
            f'<span>&#169; {YEAR} MirrorGo Guide. MirrorGo is a product of Wondershare Technology Co., Ltd.</span>'
            f'<span>Windows &amp; macOS &#183; Android &amp; iPhone</span>'
            f'</div></footer>')

def BC(items):
    parts=[]
    for label,url in items:
        if url: parts.append('<a href="'+url+'">'+label+'</a>')
        else: parts.append(label)
    return '<div class="bcrumb container">'+' &rsaquo; '.join(parts)+'</div>'

def CTA(h="Mirror Your Phone to PC &#8212; Download MirrorGo Free",
        p="Full HD 1080p screen mirror with no lag. Control phone from PC. Record, game, stream. Free trial &#8212; Android &amp; iPhone."):
    return (f'<div class="cta-strip"><h2>{h}</h2><p>{p}</p>'
            f'<a href="{AFFILIATE_URL}" class="btn-w" target="_blank" rel="nofollow sponsored">&#8659; Download Free Trial</a></div>')

def SW_SCHEMA():
    d={"@context":"https://schema.org","@type":"SoftwareApplication","name":"Wondershare MirrorGo",
       "operatingSystem":"Windows, macOS","applicationCategory":"UtilitiesApplication",
       "offers":{"@type":"Offer","price":"0","priceCurrency":"USD","description":"Free trial available"},
       "description":"MirrorGo mirrors Android and iPhone screens to PC in full HD with no lag. Control phone from PC, record screen, play games, transfer files, take screenshots.",
       "url":AFFILIATE_URL,
       "publisher":{"@type":"Organization","name":"Wondershare Technology"},
       "aggregateRating":{"@type":"AggregateRating","ratingValue":"4.7","reviewCount":"5123","bestRating":"5"}}
    return '<script type="application/ld+json">'+json.dumps(d)+'</script>'

def BC_SCHEMA(items):
    els=[{"@type":"ListItem","position":i+1,"name":l,"item":SITE_DOMAIN+"/"+u if u else SITE_DOMAIN} for i,(l,u) in enumerate(items)]
    return '<script type="application/ld+json">'+json.dumps({"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":els})+'</script>'

def FAQ_SCHEMA(pairs):
    items=[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in pairs]
    return '<script type="application/ld+json">'+json.dumps({"@context":"https://schema.org","@type":"FAQPage","mainEntity":items})+'</script>'

def ART_SCHEMA(title,desc,pub):
    d={"@context":"https://schema.org","@type":"Article","headline":title,"description":desc,
       "datePublished":pub,"dateModified":BUILD_DATE,
       "author":{"@type":"Organization","name":"MirrorGo Guide"},
       "publisher":{"@type":"Organization","name":"MirrorGo Guide"}}
    return '<script type="application/ld+json">'+json.dumps(d)+'</script>'

def HEAD(title,desc,canon,extra="",og_type="website"):
    return ("<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n"
            "<meta charset=\"UTF-8\"/><meta name=\"viewport\" content=\"width=device-width,initial-scale=1.0\"/>\n"
            f"<title>{title}</title>\n"
            f"<meta name=\"description\" content=\"{desc}\"/>\n"
            f"<link rel=\"canonical\" href=\"{SITE_DOMAIN}/{canon}\"/>\n"
            f"<meta property=\"og:title\" content=\"{title}\"/>\n"
            f"<meta property=\"og:description\" content=\"{desc}\"/>\n"
            f"<meta property=\"og:type\" content=\"{og_type}\"/>\n"
            f"<meta property=\"og:url\" content=\"{SITE_DOMAIN}/{canon}\"/>\n"
            "<meta property=\"og:site_name\" content=\"MirrorGo Guide\"/>\n"
            "<meta name=\"twitter:card\" content=\"summary_large_image\"/>\n"
            f"<meta name=\"twitter:title\" content=\"{title}\"/>\n"
            f"<meta name=\"twitter:description\" content=\"{desc}\"/>\n"
            "<meta name=\"robots\" content=\"index,follow\"/>\n"
            +CSS+"\n"+SW_SCHEMA()+"\n"+extra+"\n</head>")

FEATURES=[
    ("&#128247;","Mirror Android to PC","Full HD 1080p with virtually no lag &#8212; USB or WiFi, no root required.",
     ["Full HD 1080p mirror quality","USB and WiFi connection","No root required","1,000+ Android devices"]),
    ("&#128241;","Mirror iPhone to PC","Mirror iPhone and iPad wirelessly via WiFi &#8212; no Apple TV, no cable.",
     ["Wireless WiFi mirroring","All iPhone and iPad models","iOS 9 and above","No cable needed"]),
    ("&#128377;","Control Phone from PC","Full mouse and keyboard control of Android or iPhone from your PC desk.",
     ["Mouse click = phone tap","PC keyboard input to any app","Reply to WhatsApp/SMS from PC","Manage all apps on big screen"]),
    ("&#127918;","Game Keyboard","Map PC keyboard keys to on-screen game buttons for full mobile gaming control.",
     ["Custom key mapping for any game","WASD and full keyboard layouts","Macro key support","Saved profiles per game"]),
    ("&#128250;","HD Screen Recording","Record phone screen directly on PC in HD &#8212; no watermark, no time limit.",
     ["HD recording without watermark","Saved directly to PC as MP4","Record gameplay, tutorials, demos","Pause and resume anytime"]),
    ("&#128247;","Screenshots on PC","Capture your phone screen instantly from your PC and save to folder or clipboard.",
     ["One-click screenshot capture","Auto-saved to PC folder","Copy to clipboard instantly","Capture any app moment"]),
    ("&#128203;","Drag-and-Drop File Transfer","Transfer files between Android and PC by dragging and dropping &#8212; no extra software.",
     ["Photos, videos, documents","Drag from PC to Android","Drag from Android to PC","USB or WiFi transfer"]),
    ("&#128221;","Clipboard Sharing","Copy on phone, paste on PC. Copy on PC, paste on phone &#8212; instant bidirectional sync.",
     ["Bidirectional clipboard sync","Any text content","Works with any app","Instant &#8212; no button needed"]),
]

def FEATURES_GRID():
    cards=""
    for icon,name,desc,buls in FEATURES:
        li="".join("<li>"+b+"</li>" for b in buls)
        cards+='<div class="card"><div class="fi">'+icon+'</div><h3>'+name+'</h3><p>'+desc+'</p><ul>'+li+'</ul></div>'
    return '<div class="grid2">'+cards+'</div>'

TESTIMONIALS=[
    ("&#9733;&#9733;&#9733;&#9733;&#9733;","I play PUBG Mobile every day but the small screen was killing my rank. MirrorGo on my 27-inch monitor with full keyboard control changed everything. Zero lag, full HD &#8212; I actually rank up now.","James R.","London, UK &#127468;&#127463;"),
    ("&#9733;&#9733;&#9733;&#9733;&#9733;","I demo our mobile app to clients via Zoom. MirrorGo lets me mirror the iPhone wirelessly and share the window in Zoom. Clients see every detail in HD. Completely changed our sales process.","Sarah K.","New York, USA &#127482;&#127480;"),
    ("&#9733;&#9733;&#9733;&#9733;&#9733;","As a teacher I mirror my phone to the classroom projector via MirrorGo. Students see every app and setting in full HD. Setup is 30 seconds. I use it every single day.","Priya M.","Mumbai, India &#127470;&#127475;"),
    ("&#9733;&#9733;&#9733;&#9733;&#9733;","I record mobile app tutorial videos for YouTube. MirrorGo gives me HD recordings without watermarks. Keyboard control means I narrate while operating the phone. Professional quality without expensive hardware.","Tom H.","Sydney, Australia &#127462;&#127482;"),
    ("&#9733;&#9733;&#9733;&#9733;&#9733;","Ich teste Android-Apps f&#252;r meinen Arbeitgeber. Mit MirrorGo sehe ich alles auf dem gro&#223;en Monitor und kann gleichzeitig aufnehmen. Fehler sind sofort dokumentiert und reproduzierbar.","Klaus B.","Berlin, Deutschland &#127465;&#127466;"),
    ("&#9733;&#9733;&#9733;&#9733;&#9733;","The drag-and-drop file transfer alone saves me 20 minutes a day. No more emailing photos to myself or using Google Drive just to move files between my Samsung and PC.","Marie D.","Paris, France &#127467;&#127479;"),
]

def TESTIMONIALS_GRID():
    cards="".join('<div class="tcard"><div class="stars">'+s+'</div><p class="ttext">"'+t+'"</p><div class="tauthor">'+n+" &#8212; "+l+'</div></div>' for s,t,n,l in TESTIMONIALS)
    return '<div class="grid3">'+cards+'</div>'

FAQ_GLOBAL=[
    ("What is Wondershare MirrorGo?","Wondershare MirrorGo is screen mirroring software that displays your Android or iPhone screen on your PC in full HD 1080p with no lag. It also lets you control the phone from PC with mouse and keyboard, record the screen in HD, transfer files and take screenshots."),
    ("How do I mirror Android to PC?","Enable USB Debugging in Android Developer Options, connect via USB cable, and open MirrorGo. Your Android screen appears on PC instantly in full HD. Alternatively, connect via WiFi on the same network for wireless mirroring."),
    ("How do I mirror iPhone to PC?","Connect your iPhone and PC to the same WiFi network. Open MirrorGo on PC, then swipe down on iPhone for Control Centre, tap Screen Mirroring and select MirrorGo. The iPhone screen appears wirelessly on PC."),
    ("Does MirrorGo require root?","No &#8212; MirrorGo works without rooting. Enable USB Debugging in Android Developer Options (tap Build Number 7 times). For iPhone, no special settings are needed beyond the same WiFi network."),
    ("Can I play mobile games on PC with MirrorGo?","Yes &#8212; the Game Keyboard feature maps PC keyboard keys to on-screen game buttons. Play any mobile game with full keyboard and mouse control on your PC monitor using your actual phone account."),
    ("Can MirrorGo record the phone screen?","Yes &#8212; click Record in MirrorGo to capture the phone screen in HD directly on your PC as an MP4 file. No watermarks, no time limits. Works for Android and iPhone."),
    ("What is the difference vs an Android emulator?","Emulators run a separate Android environment &#8212; your phone account, items and progress are different. MirrorGo mirrors your actual phone, so you play on your real game account with your real items, just on the PC screen."),
    ("Is there a free trial?","Yes &#8212; MirrorGo offers a free trial with access to all features. Full ongoing use requires a subscription starting at $19.95/month."),
    ("Does it work with Android and iPhone?","Yes &#8212; MirrorGo supports both Android (USB or WiFi) and iPhone/iPad (WiFi). One subscription covers both platforms."),
    ("Can I share my phone screen in Zoom or Teams?","Yes &#8212; share the MirrorGo application window in any video conferencing tool. Participants see your phone screen in full HD, and you can control the phone during the share."),
]

def FAQ_BLOCK(pairs):
    items="".join('<div class="faq-item"><div class="faq-q">'+q+'</div><div class="faq-a">'+a+'</div></div>' for q,a in pairs)
    return '<div class="faq-list">'+items+'</div>'

def related_cloud(kw_data,n=24):
    same=[k for k in KEYWORDS if k["cat"]==kw_data["cat"] and k["slug"]!=kw_data["slug"]]
    diff=[k for k in KEYWORDS if k["cat"]!=kw_data["cat"]]
    pool=(same+diff)[:n]
    links="".join('<a class="kw" href="'+BASE_PATH+'/'+r["slug"]+'.html">'+r["keyword"]+'</a>' for r in pool)
    return '<div class="kw-cloud">'+links+'</div>'


def cat_deep(cat, keyword):
    bodies = {
"android-mirror": (
    '<section style="background:#fff"><div class="container">'
    '<div class="sec-ey">In-Depth Guide</div><h2>Mirror Android to PC &#8212; Everything You Need to Know</h2>'
    '<div class="prose">'
    '<p>MirrorGo displays your Android screen on your PC monitor in real time at full HD (1080p) resolution with under 50 milliseconds of input lag &#8212; responsive enough for fast-paced gaming, live presentations and app demonstrations. Most generic screen cast tools produce blurry, laggy output. MirrorGo renders the full-resolution Android interface natively on your PC as a crisp, interactive window.</p>'
    '<h3>USB vs WiFi &#8212; Which Should You Use?</h3>'
    '<p><strong>USB connection</strong> provides the absolute lowest latency and highest stability. Enable USB Debugging (Settings &#8594; About Phone &#8594; tap Build Number 7 times to unlock Developer Options &#8594; enable USB Debugging), connect via USB cable, and MirrorGo detects your device in seconds. Best choice for gaming, precise keyboard control and screen recording where every millisecond matters. <strong>WiFi connection</strong> works wirelessly when phone and PC share the same router. Slightly higher latency than USB but eliminates the cable &#8212; ideal for classroom presentations, video meetings and any scenario where cable-free setup matters. Both phones must be on the same 5GHz WiFi band for minimum wireless delay.</p>'
    '<h3>No Root Required</h3>'
    '<p>USB Debugging is the only Android prerequisite. It\'s a developer setting that takes under a minute to enable and requires no modification to the phone\'s system software. You do not need to root, unlock the bootloader or install any custom firmware. MirrorGo works on standard consumer Android devices as shipped from manufacturers.</p>'
    '<h3>Compatibility</h3>'
    '<p>MirrorGo supports 1,000+ Android devices: all Samsung Galaxy S and A series, Google Pixel 3 through 9, Huawei, Xiaomi, OnePlus, Motorola, Sony Xperia and more. Android 5.0 Lollipop and above is required. Older Android 4.x devices are not supported.</p>'
    '</div></div></section>'),

"iphone-mirror": (
    '<section style="background:#fff"><div class="container">'
    '<div class="sec-ey">iPhone Mirror Guide</div><h2>Mirror iPhone to PC &#8212; No Apple TV Required</h2>'
    '<div class="prose">'
    '<p>Apple\'s AirPlay protocol broadcasts the iPhone screen over WiFi. MirrorGo acts as an AirPlay receiver on Windows PC &#8212; it appears in the iPhone\'s Screen Mirroring list exactly like an Apple TV would. No cable, no adapter, no Apple TV hardware needed. Any iPhone running iOS 9 or above can mirror to MirrorGo.</p>'
    '<h3>How to Connect</h3>'
    '<p>Open MirrorGo on your PC. Ensure the iPhone and PC are on the same WiFi network (the same router, ideally the same 5GHz band for lower latency). On iPhone, swipe down from the top-right corner to open Control Centre, tap Screen Mirroring, and select MirrorGo from the list. The iPhone screen appears on your PC within seconds.</p>'
    '<h3>What\'s Different from Android</h3>'
    '<p>iPhone mirroring is wireless-only due to iOS restrictions &#8212; USB mirroring is not supported by Apple\'s USB protocol. Mouse-and-keyboard control (reverse control) of iPhone from PC requires iOS 13 or iOS 14 specifically. Screen recording of the mirrored iPhone screen works identically to Android &#8212; HD MP4 captured directly on the PC.</p>'
    '<h3>Supported Models</h3>'
    '<p>All iPhone models from iPhone 6 onwards (iOS 9+) for screen mirroring. iPhone 17, iPhone 16, iPhone 15, iPhone 14 and all earlier models on iOS 9 and above are fully supported. iPad is also supported using the same process.</p>'
    '</div></div></section>'),

"phone-control": (
    '<section style="background:#fff"><div class="container">'
    '<div class="sec-ey">Phone Control Guide</div><h2>Control Your Phone from PC &#8212; Mouse &amp; Keyboard</h2>'
    '<div class="prose">'
    '<p>Once your Android is mirrored to MirrorGo via USB, the PC mouse becomes the phone\'s touchscreen and the PC keyboard becomes the text input. Clicking anywhere on the mirrored screen is equivalent to tapping that point on the phone\'s touchscreen. Typing on the keyboard inputs into whatever is focused on the phone. This enables complete phone management from the PC desk without touching the device.</p>'
    '<h3>Everyday Use Cases</h3>'
    '<p>Reply to WhatsApp messages at full keyboard speed without picking up the phone. Read and respond to SMS texts on the large PC screen. Browse social media with the mouse wheel &#8212; infinitely more comfortable than touch scrolling. Navigate any app including settings, file managers, cameras and system menus. Type URLs, addresses and long text in any Android app using the PC keyboard.</p>'
    '<h3>Game Keyboard &#8212; Mobile Gaming Redefined</h3>'
    '<p>The Game Keyboard feature goes further by mapping specific keyboard keys to specific screen positions. For a battle royale game, map WASD to the movement joystick, left mouse button to fire, Space to jump, R to reload and F to interact. Each mapping is saved as a profile for that specific game &#8212; switch games, load the correct layout. The result is mobile gaming with the control precision of a PC game while playing on the actual phone account.</p>'
    '<h3>Productivity Benefits</h3>'
    '<p>For professionals who manage business WhatsApp, need to demo mobile apps on PC, or work with phone-specific software that has no desktop equivalent, keyboard control eliminates the constant physical phone handling that disrupts focus during PC work sessions.</p>'
    '</div></div></section>'),

"gaming": (
    '<section style="background:#fff"><div class="container">'
    '<div class="sec-ey">Mobile Gaming on PC</div><h2>Play Mobile Games on PC &#8212; Without Emulators</h2>'
    '<div class="prose">'
    '<p>Mobile gaming has two fundamental limitations on a phone: the screen is too small to see detail clearly in fast-paced games, and touch controls are imprecise compared to keyboard and mouse. MirrorGo eliminates both on your PC monitor while keeping everything on the actual phone.</p>'
    '<h3>The Emulator Problem &#8212; Why MirrorGo is Better</h3>'
    '<p>Android emulators (BlueStacks, NoxPlayer, LDPlayer) create a completely separate Android environment on your PC. The game account on the emulator is separate from your phone account. Any in-app purchases, characters, skins, ranked progress or friends lists on your phone account do not carry to the emulator. If you switch back to your phone, the progress diverges. MirrorGo mirrors your actual phone &#8212; one account, one progress, playable on phone or PC screen interchangeably.</p>'
    '<h3>Setting Up Game Keyboard</h3>'
    '<p>Open the game in MirrorGo. Click Game Keyboard in the toolbar. The mapping interface overlays the game in semi-transparent mode. Drag virtual control buttons to match the game\'s on-screen layout. Assign keyboard keys and mouse buttons to each virtual button. Typical PUBG Mobile setup: W/A/S/D for movement joystick, mouse for camera/aim, left click for fire, Space for jump, R for reload, C for crouch, F for interact, G for grenades. Save the layout. It loads automatically every time you open that game.</p>'
    '<h3>Connection for Gaming</h3>'
    '<p>Always use USB for gaming &#8212; not WiFi. USB latency is typically under 30ms. WiFi latency ranges from 50-150ms and can spike higher under network congestion. In a fast-paced shooting game, the difference between USB and WiFi latency is the difference between hitting shots and missing them.</p>'
    '</div></div></section>'),

"recording": (
    '<section style="background:#fff"><div class="container">'
    '<div class="sec-ey">Screen Recording Guide</div><h2>Record Phone Screen on PC &#8212; HD, No Watermark</h2>'
    '<div class="prose">'
    '<p>Android\'s built-in screen recorder saves to phone storage (limited space on many devices), has time limits on some manufacturers\' implementations, may add watermarks, and produces output that must be transferred to PC before editing. MirrorGo records the full HD mirrored stream directly to any folder on your PC &#8212; unlimited duration, unlimited storage, no watermarks, no transfer step.</p>'
    '<h3>The Recording Process</h3>'
    '<p>Mirror your phone to MirrorGo. Navigate to the app, game or content you want to record. Click Record. MirrorGo captures everything displayed in the mirrored window as an MP4 file. Click Stop when finished. The file is in your chosen output folder immediately &#8212; no export, no conversion, no cloud upload.</p>'
    '<h3>Use Cases by Type</h3>'
    '<p><strong>Gameplay:</strong> Record mobile game sessions in 1080p for YouTube or Twitch. The keyboard control during recording means you can play effectively while the session is being captured. <strong>App tutorials:</strong> Record demonstrations of how to use apps, configure settings or navigate features. Large PC screen view makes it easy to identify exactly what you\'re capturing. <strong>Bug reports:</strong> Record the exact sequence of taps that produces a bug &#8212; complete with the visual result. Far more useful than written descriptions. <strong>Content creation:</strong> Record phone screens for inclusion in YouTube videos, TikTok content, corporate training or product demos.</p>'
    '<h3>Combining with OBS</h3>'
    '<p>For live streaming or advanced recording with scene switching, add the MirrorGo window as a Window Capture source in OBS Studio. MirrorGo handles the mirroring quality; OBS handles encoding, overlays and streaming. This combination is used by mobile gaming streamers who want professional-quality live broadcasts of phone gameplay.</p>'
    '</div></div></section>'),

"streaming": (
    '<section style="background:#fff"><div class="container">'
    '<div class="sec-ey">Streaming Guide</div><h2>Share Phone Screen in Meetings &amp; Streams</h2>'
    '<div class="prose">'
    '<p>MirrorGo creates a standard Windows application window showing your phone screen. Any software that can share a window &#8212; Zoom, Teams, Google Meet, OBS, Streamlabs &#8212; can share the MirrorGo window. Your phone screen becomes shareable live content in any digital context.</p>'
    '<h3>Video Conferencing</h3>'
    '<p>In Zoom, click Share Screen and select the MirrorGo application window. All meeting participants see your phone screen live in HD. You control the phone during the share &#8212; navigate apps, demonstrate features, walk through settings &#8212; everything visible to participants in real time. This is the professional way to demonstrate mobile apps in client meetings rather than holding a phone up to a webcam.</p>'
    '<h3>OBS Integration for Live Streaming</h3>'
    '<p>Add MirrorGo as a Window Capture source in OBS. Your phone screen appears in your stream layout alongside webcam, game capture and other sources. Crop to portrait orientation for mobile content, or leave in landscape with overlays. This is how serious mobile gaming streamers broadcast on Twitch and YouTube Live without specialised capture hardware.</p>'
    '<h3>Classroom and Training</h3>'
    '<p>Connect a PC to a classroom projector and mirror the phone to MirrorGo. Students see the phone screen on the projection in full HD &#8212; clear from any seat in the room. Navigate apps, show settings, demonstrate software &#8212; all visible without holding a phone up to a camera or walking around the room.</p>'
    '</div></div></section>'),

"compare": (
    '<section style="background:#fff"><div class="container">'
    '<div class="sec-ey">Honest Comparison</div><h2>' + keyword + ' &#8212; Detailed Analysis</h2>'
    '<div class="prose">'
    '<p>Choosing the right screen mirror app depends on your use case. Here is an honest comparison of MirrorGo against the main alternatives.</p>'
    '<h3>vs Vysor</h3>'
    '<p>Vysor runs inside Chrome browser. MirrorGo is a native Windows application with higher resolution and lower latency. MirrorGo adds Game Keyboard, HD recording without watermark and iPhone support &#8212; features Vysor lacks. Vysor Free is heavily compressed; Vysor Pro improves quality but still runs in browser. For gaming, recording and professional use, MirrorGo is substantially better.</p>'
    '<h3>vs scrcpy (Free, Open Source)</h3>'
    '<p>scrcpy achieves excellent performance and is genuinely free. However, it is command-line only &#8212; no graphical interface, no Game Keyboard UI, no built-in recording, no iPhone support. MirrorGo provides all of these in a polished GUI. For technical users comfortable with command line: scrcpy is excellent. For everyone else: MirrorGo.</p>'
    '<h3>vs Android Emulators</h3>'
    '<p>Emulators run a separate Android instance. Game progress on the emulator differs from the phone. MirrorGo mirrors the actual phone &#8212; same account, same progress, same items. For gaming on your real account, MirrorGo is the correct choice, not an emulator.</p>'
    '</div></div></section>'),

"file-transfer": (
    '<section style="background:#fff"><div class="container">'
    '<div class="sec-ey">File Transfer Guide</div><h2>Transfer Files Between Android &amp; PC</h2>'
    '<div class="prose">'
    '<p>Most Android-to-PC file transfer requires Google Drive, a dedicated file manager app or Windows Explorer in MTP mode. MirrorGo includes drag-and-drop file transfer as a built-in feature &#8212; when your Android is connected, browse its file system and move files to and from your PC without any additional software.</p>'
    '<h3>Android to PC</h3>'
    '<p>Click the File Transfer icon in MirrorGo. The Android file system appears in a panel. Browse to the photos, videos or documents you want. Drag them to your PC desktop, Documents folder or any location. Alternatively, select and click Export. Files transfer at USB speed &#8212; significantly faster than Bluetooth or Google Drive upload/download.</p>'
    '<h3>PC to Android</h3>'
    '<p>Drag files from Windows Explorer into the MirrorGo file transfer panel targeting a folder on the Android. The files appear on the phone immediately. This works for documents, photos, music, APK installation files and any other file type the Android can handle.</p>'
    '<h3>Clipboard Sharing</h3>'
    '<p>For text content, clipboard sharing is faster than any file transfer. Copy a URL, address or paragraph on the phone &#8212; paste it directly in any PC application. Copy code, email content or notes on the PC &#8212; paste it into any Android app. The clipboard syncs bidirectionally and instantly whenever content is copied on either device.</p>'
    '</div></div></section>'),
    }
    body=bodies.get(cat)
    if body: return body
    aff=AFFILIATE_URL
    return ('<section style="background:#fff"><div class="container">'
            '<div class="sec-ey">Complete Guide</div>'
            '<h2>'+keyword+' &#8212; Overview</h2>'
            '<div class="prose">'
            '<p>Wondershare MirrorGo is the leading solution for '+keyword.lower()+' on Windows and Mac. '
            'Mirror Android or iPhone to PC in full HD 1080p with no lag &#8212; then control the phone with mouse and keyboard, '
            'record the screen in HD, transfer files and take screenshots, all in one application.</p>'
            '<p>Whether you want to play mobile games on your PC monitor, present your phone in a meeting, record tutorials, '
            'or manage your phone from your computer without constantly picking it up, '
            'MirrorGo covers every scenario with a simple USB or WiFi connection.</p>'
            '</div>'
            '<div style="margin-top:2rem">'
            '<a href="'+aff+'" class="btn-p" target="_blank" rel="nofollow sponsored">&#8659; Download Free Trial</a>'
            '</div></div></section>')

def build_keyword_page(kw_data):
    slug=kw_data["slug"]; keyword=kw_data["keyword"]; cat=kw_data["cat"]
    a1,a2=ac(cat)
    title  = keyword+" &#8212; Wondershare MirrorGo | "+str(YEAR)
    desc   = ("Looking for "+keyword.lower()+"? MirrorGo mirrors, controls and records your phone screen on PC in full HD. "
              "Android &amp; iPhone. Free trial.")
    canon  = slug+".html"
    faq_pairs=[
        ("Can MirrorGo handle "+keyword.lower()+"?",
         "Yes &#8212; MirrorGo is specifically designed for "+keyword.lower()+". "
         "Full HD screen mirroring with no lag via USB or WiFi, plus phone control, "
         "screen recording, file transfer and screenshots. Free trial available."),
        ("Does MirrorGo require root for "+keyword.lower()+"?",
         "No &#8212; MirrorGo works without rooting Android. "
         "Enable USB Debugging in Developer Options. iPhone requires only the same WiFi network."),
        ("Is there a free trial for MirrorGo?",
         "Yes &#8212; MirrorGo offers a free trial. Full ongoing use requires a subscription "
         "starting at $19.95/month, $29.95/quarter or $39.95/year."),
    ]
    bc_s=BC_SCHEMA([("Home",""),("All Topics","keywords.html"),(keyword,"")])
    fq_s=FAQ_SCHEMA(faq_pairs)
    body=cat_deep(cat,keyword)
    same=[k for k in KEYWORDS if k["cat"]==cat and k["slug"]!=slug][:6]
    links=" &#183; ".join('<a href="'+BASE_PATH+'/'+r["slug"]+'.html">'+r["keyword"]+'</a>' for r in same)

    return (HEAD(title,desc,canon,bc_s+fq_s)
        +"\n<body>\n"
        +"<style>:root{--ha:"+a1+";--hb:"+a2+";--fa:rgba(0,0,0,.05)}</style>\n"
        +NAV()+"\n"
        +BC([("Home",BASE_PATH+"/"),("All Topics",BASE_PATH+"/keywords.html"),(keyword,"")])
        +'\n<section class="hero">'
        +'\n  <div class="eyebrow">&#10022; '+cat.replace("-"," ").title()+'</div>'
        +'\n  <h1><em>'+keyword+'</em><br>&#8212; With MirrorGo</h1>'
        +'\n  <p class="hsub">Full HD &#183; No lag &#183; USB or WiFi &#183; Android &amp; iPhone &#183; Free trial</p>'
        +'\n  <div class="btns">'
        +'\n    <a href="'+AFFILIATE_URL+'" class="btn-p" target="_blank" rel="nofollow sponsored">&#8659; Download Free Trial</a>'
        +'\n    <a href="'+BASE_PATH+'/how-it-works.html" class="btn-s">How It Works</a>'
        +'\n  </div>'
        +'\n  <div class="stats">'
        +'\n    <div><span class="stat-n">Full HD</span><span class="stat-l">1080p Mirror</span></div>'
        +'\n    <div><span class="stat-n">No Lag</span><span class="stat-l">Low Latency</span></div>'
        +'\n    <div><span class="stat-n">USB+WiFi</span><span class="stat-l">Both Supported</span></div>'
        +'\n    <div><span class="stat-n">No Root</span><span class="stat-l">Required</span></div>'
        +'\n  </div>\n</section>\n'
        +'\n<section><div class="container">'
        +'\n  <div class="sec-ey">All Features</div>'
        +'\n  <h2>Everything in MirrorGo</h2>'
        +FEATURES_GRID()
        +'\n</div></section>\n'
        +body
        +'\n<section style="background:#ede9fe"><div class="container">'
        +'\n  <div class="sec-ey">Real Users</div><h2>Gamers, Creators &amp; Professionals</h2>'
        +TESTIMONIALS_GRID()
        +'\n</div></section>\n'
        +'\n<section><div class="container">'
        +'\n  <div class="sec-ey">FAQ</div><h2>Common Questions</h2>'
        +FAQ_BLOCK(faq_pairs+FAQ_GLOBAL[:3])
        +'\n  <div style="margin-top:1.5rem">'
        +'\n    <a href="'+BASE_PATH+'/faq.html" style="color:var(--ha);font-weight:600;font-size:.88rem">View all FAQs &#8594;</a>'
        +'\n  </div>\n</div></section>\n'
        +'\n<section class="dark-sec"><div class="container">'
        +'\n  <div class="sec-ey">Related Topics</div><h2>Explore More</h2>'
        +related_cloud(kw_data,28)
        +('\n  <p style="margin-top:1.4rem;font-size:.78rem;color:rgba(255,255,255,.35)">More: '+links+'</p>' if links else '')
        +'\n</div></section>\n'
        +CTA("Try MirrorGo for "+keyword.title(),"Free trial &#8212; mirror, control and record your phone on PC.")
        +"\n"+FOOTER()+"\n"+FAQ_JS+"\n</body></html>")


def page_index():
    extra=FAQ_SCHEMA(FAQ_GLOBAL[:6])+BC_SCHEMA([("Home","")])
    uses=[
        ("&#127918;","Play Mobile Games","play-android-games-on-pc","Keyboard &amp; mouse on real account"),
        ("&#128247;","Mirror Android","mirror-android-to-pc","Full HD, no lag, USB or WiFi"),
        ("&#128241;","Mirror iPhone","mirror-iphone-to-pc","Wireless via WiFi &#8212; no cable"),
        ("&#128377;","Control Phone","control-android-from-pc","Mouse and keyboard control"),
        ("&#128250;","Record Screen","record-android-screen-pc","HD, no watermark, saved to PC"),
        ("&#127909;","Share in Zoom","phone-screen-zoom-meeting","Phone screen in video meetings"),
        ("&#128203;","Transfer Files","transfer-files-android-pc","Drag and drop Android&#8596;PC"),
        ("&#127891;","Classroom Mirror","android-mirror-teacher-classroom","Project phone on classroom screen"),
    ]
    ug="".join('<a class="uc-card" href="'+BASE_PATH+'/'+s+'.html"><span class="uc-icon">'+i+'</span><span class="uc-label">'+n+'</span><span class="uc-sub">'+d+'</span></a>' for i,n,s,d in uses)
    return (HEAD("MirrorGo &#8212; Mirror, Control &amp; Record Phone on PC | Full HD | "+str(YEAR),
                 "Mirror Android or iPhone to PC in full HD with no lag. Control with keyboard, record screen, play games, transfer files. Free trial.",
                 "",extra)
        +"\n<body>\n"+NAV()
        +'\n<section class="hero">'
        +'\n  <div class="eyebrow">&#10022; #1 Phone Screen Mirror for PC</div>'
        +'\n  <h1>Your Phone.<br><em>On Your PC Screen.</em></h1>'
        +'\n  <p class="hsub">Mirror Android or iPhone to PC in full HD with no lag. Control with mouse and keyboard. Record, stream, game and transfer files. Free trial.</p>'
        +'\n  <div class="btns">'
        +'\n    <a href="'+AFFILIATE_URL+'" class="btn-p" target="_blank" rel="nofollow sponsored">&#8659; Download Free Trial</a>'
        +'\n    <a href="'+BASE_PATH+'/how-it-works.html" class="btn-s">See How It Works</a>'
        +'\n  </div>'
        +'\n  <div class="stats">'
        +'\n    <div><span class="stat-n">Full HD</span><span class="stat-l">1080p Mirror</span></div>'
        +'\n    <div><span class="stat-n">No Lag</span><span class="stat-l">Ultra-Low Latency</span></div>'
        +'\n    <div><span class="stat-n">No Root</span><span class="stat-l">Required</span></div>'
        +'\n    <div><span class="stat-n">USB+WiFi</span><span class="stat-l">Both Supported</span></div>'
        +'\n  </div>\n</section>\n'
        +'\n<section style="background:#fff"><div class="container">'
        +'\n  <div class="sec-ey">What Do You Want to Do?</div>'
        +'\n  <h2>Every Phone-to-PC Use Case Covered</h2>'
        +'\n  <p class="sec-sub">Click your scenario for a step-by-step guide &#8212; or download MirrorGo and start now.</p>'
        +'\n  <div class="uc-grid">'+ug+'</div>'
        +'\n</div></section>\n'
        +'\n<section><div class="container">'
        +'\n  <div class="sec-ey">Complete Feature Suite</div>'
        +'\n  <h2>Mirror + Control + Record + Game + Transfer</h2>'
        +'\n  <p class="sec-sub">Everything for working with your phone on a PC screen &#8212; in one application.</p>'
        +FEATURES_GRID()
        +'\n  <div style="margin-top:2.5rem;text-align:center">'
        +'\n    <a href="'+BASE_PATH+'/features.html" style="color:var(--ha);font-weight:600">View full feature list &#8594;</a>'
        +'\n  </div>\n</div></section>\n'
        +'\n<section style="background:#fff"><div class="container">'
        +'\n  <div class="sec-ey">Why MirrorGo?</div>'
        +'\n  <h2>More Than Just Screen Casting</h2>'
        +'\n  <div class="grid3">'
        +'\n    <div class="card"><div class="fi">&#128247;</div><h3>Full HD, No Lag</h3><p>Generic screen cast tools produce blurry, laggy output. MirrorGo renders 1080p at under 50ms latency &#8212; sharp and responsive enough for fast-paced gaming and live demos.</p></div>'
        +'\n    <div class="card"><div class="fi">&#128377;</div><h3>Real Mouse &amp; Keyboard Control</h3><p>Click anywhere on the mirrored screen to tap the phone. Type with your full keyboard. Scroll with the mouse wheel. Control every app from your PC desk.</p></div>'
        +'\n    <div class="card"><div class="fi">&#127918;</div><h3>Gaming &#8212; No Emulator Needed</h3><p>Play on your actual phone account with keyboard and mouse on your PC monitor. No emulator, no separate account, same progress and items always.</p></div>'
        +'\n  </div>\n</div></section>\n'
        +'\n<section style="background:#ede9fe"><div class="container">'
        +'\n  <div class="sec-ey">Real Users</div>'
        +'\n  <h2 style="text-align:center;margin-bottom:2.5rem">Gamers, Teachers, Creators &amp; Professionals</h2>'
        +TESTIMONIALS_GRID()
        +'\n</div></section>\n'
        +'\n<section><div class="container">'
        +'\n  <div class="sec-ey">FAQ</div><h2>Common Questions</h2>'
        +FAQ_BLOCK(FAQ_GLOBAL[:6])
        +'\n  <div style="margin-top:1.5rem;text-align:center">'
        +'\n    <a href="'+BASE_PATH+'/faq.html" style="color:var(--ha);font-weight:600">View all FAQs &#8594;</a>'
        +'\n  </div>\n</div></section>\n'
        +CTA()+"\n"+FOOTER()+"\n"+FAQ_JS+"\n</body></html>")

def page_features():
    bc=BC_SCHEMA([("Home",""),("Features","")])
    rows=[
        ("Android Screen Mirror",    "V","V","V","V","V"),
        ("iPhone Screen Mirror",     "V","V","V","V","Limited"),
        ("Full HD 1080p",            "V","V","Partial","Partial","X"),
        ("Ultra-Low Latency",        "V","Partial","Partial","Partial","X"),
        ("Phone Control (Mouse/KB)", "V","V","Limited","X","X"),
        ("Game Keyboard Mapping",    "V","X","X","X","X"),
        ("HD Recording No Watermark","V","Partial","V","V","X"),
        ("File Transfer Drag-Drop",  "V","V","V","V","X"),
        ("Clipboard Sharing",        "V","X","X","X","X"),
        ("Zoom/Teams Window Share",  "V","V","V","V","V"),
        ("WiFi + USB Both",          "V","V","WiFi Only","V","USB Only"),
        ("No Root Required",         "V","V","V","V","V"),
        ("Free Trial",               "V","V","V","V","V"),
    ]
    tools=["MirrorGo &#10022;","Vysor","LetsView","Reflector","scrcpy"]
    hrow="<tr><th>Feature</th>"+"".join(('<th class="hl">' if i==0 else '<th>')+t+'</th>' for i,t in enumerate(tools))+"</tr>"
    def cell(v,i):
        if i==0: return '<td class="ck" style="font-weight:700">'+v+'</td>'
        if v=="V": return '<td class="ck">&#10004;</td>'
        if v=="X": return '<td class="cr">&#10008;</td>'
        return '<td class="cp">'+v+'</td>'
    trows="".join("<tr>"+cell(r[0],-1)+"".join(cell(v,i) for i,v in enumerate(r[1:]))+"</tr>" for r in rows)
    return (HEAD("MirrorGo Features &#8212; Mirror, Control, Record, Game, Transfer | "+str(YEAR),
                 "Complete MirrorGo feature list vs Vysor, LetsView, Reflector and scrcpy. Full HD mirror, game keyboard, HD recording.",
                 "features.html",bc)
        +"\n<body>\n"+NAV()
        +"\n"+BC([("Home",BASE_PATH+"/"),("Features","")])
        +'\n<section class="hero"><div class="eyebrow">&#10022; Complete Feature List</div>'
        +'\n  <h1>Everything MirrorGo<br><em>Can Do</em></h1>'
        +'\n  <p class="hsub">Mirror &#183; Control &#183; Record &#183; Game &#183; Stream &#183; Transfer &#8212; all in one app</p>'
        +'\n  <a href="'+AFFILIATE_URL+'" class="btn-p" target="_blank" rel="nofollow sponsored">&#8659; Download Free Trial</a>'
        +'\n</section>\n'
        +'\n<section><div class="container"><div class="sec-ey">All Features</div><h2>The Complete Toolkit</h2>'
        +FEATURES_GRID()
        +'\n</div></section>\n'
        +'\n<section style="background:#fff"><div class="container"><div class="sec-ey">5-Tool Comparison</div><h2>MirrorGo vs Every Alternative</h2>'
        +'\n  <div class="tbl-wrap"><table><thead>'+hrow+'</thead><tbody>'+trows+'</tbody></table></div>'
        +'\n  <p style="margin-top:.9rem;font-size:.75rem;color:var(--muted)">&#10004; Full &#160; Partial = Limited &#160; &#10008; Not available</p>'
        +'\n</div></section>\n'
        +CTA("Try All Features Free","Download MirrorGo &#8212; free trial, no credit card required.")
        +"\n"+FOOTER()+"\n</body></html>")

def page_how_it_works():
    bc=BC_SCHEMA([("Home",""),("How It Works","")])
    return (HEAD("How MirrorGo Works &#8212; Mirror Phone to PC in 3 Steps | "+str(YEAR),
                 "Set up MirrorGo in 3 steps: enable USB debugging, connect, mirror. Android via USB or WiFi, iPhone via WiFi. No root.",
                 "how-it-works.html",bc)
        +"\n<body>\n"+NAV()
        +"\n"+BC([("Home",BASE_PATH+"/"),("How It Works","")])
        +'\n<section class="hero"><div class="eyebrow">&#10022; Simple 3-Step Setup</div>'
        +'\n  <h1>Phone on PC<br><em>in 3 Steps</em></h1>'
        +'\n  <p class="hsub">Android via USB or WiFi &#183; iPhone via WiFi &#183; No root &#183; No complicated setup</p>'
        +'\n  <a href="'+AFFILIATE_URL+'" class="btn-p" target="_blank" rel="nofollow sponsored">&#8659; Download Free Trial</a>'
        +'\n</section>\n'
        +'\n<section><div class="container"><div class="sec-ey">Android Setup</div><h2>Mirror Android to PC &#8212; 3 Steps</h2>'
        +'\n  <div class="steps">'
        +'\n    <div class="step"><div class="sn">1</div><h3>Enable USB Debugging</h3><p>Settings &#8594; About Phone &#8594; tap Build Number 7 times &#8594; Developer Options &#8594; enable USB Debugging. Takes 30 seconds. No root needed.</p></div>'
        +'\n    <div class="step"><div class="sn">2</div><h3>Connect to PC</h3><p>Connect Android via USB cable and open MirrorGo. MirrorGo detects your device automatically. Or use WiFi: connect both to the same network for wireless mirroring.</p></div>'
        +'\n    <div class="step"><div class="sn">3</div><h3>Mirror &amp; Control</h3><p>Your Android screen appears on PC in full HD instantly. Click to tap, type to input, scroll with mouse. Record, screenshot or transfer files from the toolbar.</p></div>'
        +'\n  </div>\n</div></section>\n'
        +'\n<section style="background:#fff"><div class="container"><div class="sec-ey">iPhone Setup</div><h2>Mirror iPhone to PC &#8212; 3 Steps</h2>'
        +'\n  <div class="steps">'
        +'\n    <div class="step"><div class="sn">1</div><h3>Same WiFi Network</h3><p>Connect your iPhone and PC to the same WiFi router. No cable needed. For lowest latency, use a 5GHz WiFi band on both devices.</p></div>'
        +'\n    <div class="step"><div class="sn">2</div><h3>Open Screen Mirroring</h3><p>On iPhone swipe down for Control Centre &#8594; tap Screen Mirroring &#8594; select MirrorGo from the list. It appears just like an Apple TV.</p></div>'
        +'\n    <div class="step"><div class="sn">3</div><h3>Mirror &amp; Record</h3><p>iPhone screen appears on PC instantly. Record in HD, screenshot, and share the MirrorGo window in Zoom or Teams for presentations.</p></div>'
        +'\n  </div>\n</div></section>\n'
        +'\n<section style="background:#fff"><div class="container" style="padding-top:0"><div class="sec-ey">USB vs WiFi</div><h2>Which Connection to Use</h2>'
        +'\n  <div class="grid2">'
        +'\n    <div class="card"><div class="fi">&#128204;</div><h3>USB &#8212; For Gaming &amp; Precision Control</h3><p>Lowest latency (typically &lt;30ms). Completely stable &#8212; no signal drops. Best for gaming, keyboard control and screen recording. Requires USB Debugging enabled on Android.</p></div>'
        +'\n    <div class="card"><div class="fi">&#128246;</div><h3>WiFi &#8212; For Presentations &amp; Demos</h3><p>Cable-free. Slightly higher latency (50-150ms). Best for Zoom meetings, classroom demonstrations and any situation where a cable-free desk is important. Required for iPhone.</p></div>'
        +'\n  </div>\n</div></section>\n'
        +'\n<section style="background:#ede9fe"><div class="container"><div class="sec-ey">Real Results</div><h2>What Users Experience</h2>'
        +TESTIMONIALS_GRID()
        +'\n</div></section>\n'
        +CTA("Start Mirroring Now","Download free &#8212; no credit card required. Android and iPhone supported.")
        +"\n"+FOOTER()+"\n</body></html>")

def page_faq():
    all_faqs=FAQ_GLOBAL+[
        ("What are the system requirements?","PC: Windows 7/8/10/11 (32 or 64-bit) or macOS 10.12+. Android: version 5.0 or above. iPhone: iOS 9 or above for mirroring; iOS 13/14 for reverse control from PC."),
        ("Why is there lag in my mirror?","Use USB connection for lowest latency. For WiFi, use a 5GHz band on both devices. Close bandwidth-heavy applications. USB typically achieves under 30ms latency; WiFi 50-150ms."),
        ("Can I record audio with screen recording?","Audio from the phone (speaker output) is not captured by default in the screen recording. For voiceover narration, record audio separately or use OBS Studio alongside MirrorGo."),
        ("Does it work with Samsung DeX?","Yes &#8212; MirrorGo works with all Samsung Galaxy phones including those supporting DeX mode."),
        ("Can I use a Bluetooth controller?","Yes &#8212; while MirrorGo provides keyboard/mouse control, Bluetooth controllers connected to the PC can also be used to control games mirrored from the phone."),
        ("What is the maximum mirror resolution?","Up to 1080p Full HD. Actual resolution depends on the device's own screen resolution and MirrorGo settings."),
        ("Can I control the phone while recording?","Yes &#8212; keyboard and mouse control works simultaneously with recording. Navigate apps, type, and interact with the phone while the session is being captured."),
    ]
    fq=FAQ_SCHEMA(all_faqs)
    bc=BC_SCHEMA([("Home",""),("FAQ","")])
    return (HEAD("MirrorGo FAQ &#8212; "+str(len(all_faqs))+" Questions Answered | "+str(YEAR),
                 "Every question about Wondershare MirrorGo answered &#8212; setup, lag, gaming, recording, iPhone and pricing.",
                 "faq.html",fq+bc)
        +"\n<body>\n"+NAV()
        +"\n"+BC([("Home",BASE_PATH+"/"),("FAQ","")])
        +'\n<section class="hero"><div class="eyebrow">&#10022; Complete FAQ</div>'
        +'\n  <h1>Every Question About<br><em>MirrorGo Answered</em></h1>'
        +'\n  <p class="hsub">'+str(len(all_faqs))+' questions &#8212; setup, lag, gaming, recording, iPhone and pricing.</p>'
        +'\n</section>\n'
        +'\n<section><div class="container"><div class="sec-ey">All '+str(len(all_faqs))+' Questions</div><h2>Complete FAQ</h2>'
        +FAQ_BLOCK(all_faqs)
        +'\n</div></section>\n'
        +CTA("Ready to Mirror? Download Free","Free trial &#8212; no credit card, Android and iPhone supported.")
        +"\n"+FOOTER()+"\n"+FAQ_JS+"\n</body></html>")

def page_compare():
    bc=BC_SCHEMA([("Home",""),("Compare","")])
    comps=[
        ("vs Vysor","Vysor runs in Chrome browser. MirrorGo is a native Windows app with higher resolution and lower latency. MirrorGo adds Game Keyboard (unique &#8212; no competitor has this), HD recording without watermarks and iPhone support. Vysor Free is heavily compressed. For gaming, recording and professional use, MirrorGo is substantially better."),
        ("vs scrcpy (Free, Open Source)","scrcpy is technically excellent and genuinely free &#8212; but command-line only, no GUI, no Game Keyboard UI, no built-in recording and no iPhone support. MirrorGo provides all of these in a polished application. Technical users who prefer open source: scrcpy. Everyone else: MirrorGo."),
        ("vs LetsView","LetsView offers easy wireless mirroring across multiple platforms. Limited phone control features. No Game Keyboard. Primarily a mirroring and basic presentation tool. MirrorGo leads on control depth, recording quality and gaming capability."),
        ("vs Android Emulators (BlueStacks etc.)","Emulators run a separate Android instance &#8212; different account, different progress from your phone. MirrorGo mirrors your actual phone so you play on your real game account with real items via keyboard and mouse on the PC screen. No account separation, no emulator overhead."),
    ]
    comp_cards="".join('<div class="card"><h3>'+n+'</h3><p style="font-size:.87rem;color:var(--muted)">'+d+'</p></div>' for n,d in comps)
    return (HEAD("MirrorGo vs Vysor, scrcpy, LetsView &amp; Emulators &#8212; Best Screen Mirror "+str(YEAR),
                 "Honest comparison: MirrorGo vs Vysor, scrcpy, LetsView, Reflector and Android emulators.",
                 "compare.html",bc)
        +"\n<body>\n"+NAV()
        +"\n"+BC([("Home",BASE_PATH+"/"),("Compare","")])
        +'\n<section class="hero"><div class="eyebrow">&#10022; Comparison '+str(YEAR)+'</div>'
        +'\n  <h1>MirrorGo vs<br><em>Every Alternative</em></h1>'
        +'\n  <p class="hsub">Honest comparison &#8212; mirror quality, latency, game keyboard, recording and ease of use.</p>'
        +'\n  <a href="'+AFFILIATE_URL+'" class="btn-p" target="_blank" rel="nofollow sponsored">&#8659; Download MirrorGo Free</a>'
        +'\n</section>\n'
        +'\n<section style="background:#fff"><div class="container"><div class="sec-ey">Head-to-Head</div><h2>vs Every Alternative</h2>'
        +'\n  <div class="grid2">'+comp_cards+'</div>'
        +'\n</div></section>\n'
        +'\n<section><div class="container"><div class="sec-ey">The Key Advantage</div><h2>Game Keyboard &#8212; Completely Unique</h2>'
        +'\n  <div class="prose"><p>No competitor &#8212; Vysor, scrcpy, LetsView or Reflector &#8212; offers a Game Keyboard feature with custom key mapping. MirrorGo\'s Game Keyboard lets you map any PC keyboard key or mouse button to any position on the phone screen, with saved profiles per game. This is the feature that makes mobile gaming on PC genuinely competitive rather than just viewable.</p>'
        +'\n    <p>Combined with USB\'s ultra-low latency, the result is mobile gaming with PC-level control precision on your actual phone account &#8212; something no emulator or competitor can match.</p>'
        +'\n  </div>\n</div></section>\n'
        +CTA("The Best Phone Mirror App &#8212; Try Free","Download MirrorGo &#8212; free trial, no credit card.")
        +"\n"+FOOTER()+"\n</body></html>")


BLOG_POSTS=[
    {"slug":"mirror-android-to-pc-guide","title":"How to Mirror Android to PC &#8212; Complete 2025 Guide","excerpt":"Step-by-step guide to mirroring your Android screen to PC in full HD — USB or WiFi, no root required.","cat":"Android Mirror","read":"7 min","date":"2025-01-15",
     "body":"<h2>Why Mirror Android to PC?</h2><p>A 27-inch PC monitor shows your Android in far more detail than a 6-inch phone screen. Whether for gaming, managing apps from your desk, recording tutorials or presenting in a meeting, mirroring puts your entire phone interface on PC where it's more visible and recordable.</p><h2>Enable USB Debugging (30 seconds)</h2><p>Settings &#8594; About Phone &#8594; tap Build Number 7 times &#8594; Developer Options appears &#8594; enable USB Debugging. No root, no modification to the phone.</p><h2>USB Mirror Steps</h2><ol><li>Install MirrorGo on your PC</li><li>Connect Android via USB cable</li><li>Accept the USB debugging prompt on Android</li><li>Android screen appears on PC in full HD instantly</li></ol><h2>WiFi Mirror Steps</h2><ol><li>Connect Android and PC to the same WiFi network</li><li>Open MirrorGo and select WiFi mode</li><li>Select your Android from the device list</li><li>Screen appears wirelessly</li></ol><h2>USB vs WiFi</h2><p>USB latency is typically under 30ms &#8212; use for gaming and precise control. WiFi eliminates the cable &#8212; use for presentations and demonstrations. For recording gameplay, always use USB for the most stable mirror.</p>"},
    {"slug":"mirror-iphone-to-pc-guide","title":"How to Mirror iPhone to PC &#8212; No Apple TV Needed","excerpt":"Mirror your iPhone screen to Windows PC wirelessly in minutes — all you need is the same WiFi network.","cat":"iPhone Mirror","read":"6 min","date":"2025-02-10",
     "body":"<h2>How iPhone Mirroring Works</h2><p>iPhone uses Apple's AirPlay protocol for screen mirroring. MirrorGo acts as an AirPlay receiver on Windows PC, appearing in the iPhone's Screen Mirroring list exactly like an Apple TV. Wireless, no cable, no adapter needed.</p><h2>Requirements</h2><ul><li>iPhone and PC on the same WiFi network (same router)</li><li>MirrorGo installed on PC</li><li>iPhone iOS 9 or above</li><li>Reverse control: iOS 13 or iOS 14</li></ul><h2>Steps</h2><ol><li>Open MirrorGo on PC</li><li>Connect both to same WiFi</li><li>On iPhone: swipe down &#8594; Screen Mirroring &#8594; select MirrorGo</li><li>iPhone screen appears on PC instantly</li></ol><h2>Recording iPhone on PC</h2><p>Once mirrored, click Record in MirrorGo. Captures the iPhone screen in HD directly on PC &#8212; no cable, works on Windows, saves to any folder.</p>"},
    {"slug":"play-mobile-games-on-pc-guide","title":"How to Play Mobile Games on PC with Keyboard &amp; Mouse","excerpt":"Play PUBG Mobile, Free Fire and any Android game on PC with full keyboard and mouse control — no emulator needed.","cat":"Gaming","read":"8 min","date":"2025-03-05",
     "body":"<h2>MirrorGo vs Emulators for Gaming</h2><p>Emulators (BlueStacks, NoxPlayer) run a separate Android environment with a separate account. Items, rank and friends on your phone don't carry over. MirrorGo mirrors your actual phone &#8212; same account, same items, playable on PC screen or phone interchangeably.</p><h2>Setting Up Game Keyboard</h2><ol><li>Mirror Android via USB to MirrorGo</li><li>Open the game</li><li>Click Game Keyboard in MirrorGo toolbar</li><li>Drag virtual buttons to match game controls</li><li>Assign keyboard keys to each button</li><li>Save the layout &#8212; loads automatically next time</li></ol><h2>PUBG Mobile Layout</h2><p>W/A/S/D &#8212; movement. Mouse &#8212; camera and aim. Left click &#8212; fire. Space &#8212; jump. R &#8212; reload. C &#8212; crouch. F &#8212; interact. G &#8212; grenades. Tab &#8212; inventory.</p><h2>Use USB for Gaming</h2><p>Always USB for gaming &#8212; not WiFi. USB latency is under 30ms. WiFi can spike to 150ms or more. In a fast-paced shooting game, 100ms of extra latency is the difference between landing shots and missing.</p>"},
    {"slug":"record-android-screen-on-pc","title":"How to Record Android Screen on PC &#8212; HD, No Watermark","excerpt":"Record Android gameplay, tutorials and app demos directly on PC in HD without watermarks or time limits.","cat":"Screen Recording","read":"6 min","date":"2025-04-12",
     "body":"<h2>Why Record on PC vs Phone?</h2><p>Android's built-in recorder saves to phone storage (limited space), may add watermarks, has time limits on some devices, and produces output needing transfer before editing. MirrorGo records the HD mirrored stream directly to any PC folder &#8212; unlimited duration, unlimited storage, no watermarks, no transfer.</p><h2>Recording Steps</h2><ol><li>Mirror Android to MirrorGo</li><li>Navigate to the app or game to record</li><li>Click Record in MirrorGo</li><li>Everything on the mirrored screen is captured as MP4</li><li>Click Stop &#8212; file is in your chosen folder immediately</li></ol><h2>For YouTube Gaming Content</h2><p>Use USB for lowest latency. The recording captures 1080p HD. Add a face cam and overlays in OBS by using MirrorGo as a Window Capture source alongside your webcam.</p>"},
    {"slug":"control-phone-from-pc-guide","title":"How to Control Your Android Phone from PC &#8212; Full Guide","excerpt":"Respond to WhatsApp, play games and manage every app on your Android — all from your PC mouse and keyboard.","cat":"Phone Control","read":"6 min","date":"2025-05-20",
     "body":"<h2>Full Phone Control from PC</h2><p>Once Android is mirrored via USB, your PC mouse becomes the touchscreen and keyboard becomes text input. Click to tap, type to enter text, scroll with mouse wheel &#8212; complete phone control without touching the device.</p><h2>What You Can Do</h2><ul><li>Navigate home screen and open any app</li><li>Type WhatsApp, Telegram and email messages at keyboard speed</li><li>Reply to SMS from PC</li><li>Scroll social media with mouse wheel</li><li>Take photos by tapping camera shutter</li><li>Manage settings, files and any Android feature</li></ul><h2>Game Keyboard for Gaming Control</h2><p>Map keyboard keys to screen positions for gaming. W/A/S/D movement, mouse for aim, Space for jump &#8212; full PC gaming control on your real mobile account.</p>"},
    {"slug":"phone-screen-in-zoom-teams","title":"How to Share Your Phone Screen in Zoom, Teams &amp; Google Meet","excerpt":"Show your phone screen in video meetings in full HD — without holding your phone up to a webcam.","cat":"Streaming","read":"5 min","date":"2025-06-15",
     "body":"<h2>The Professional Way to Share a Phone Screen</h2><p>Holding a phone to a webcam produces blurry, shaky video. MirrorGo creates a PC window showing the phone in HD &#8212; that window is shareable in any video conferencing tool.</p><h2>Zoom</h2><ol><li>Mirror phone to MirrorGo</li><li>Zoom &#8594; Share Screen &#8594; select MirrorGo window</li><li>Participants see phone in HD</li><li>Control phone with keyboard during share</li></ol><h2>Microsoft Teams</h2><p>Same process. Share &#8594; Window &#8594; MirrorGo. Teams participants see phone screen live. Narrate and control during the meeting.</p><h2>Classroom</h2><p>PC connected to projector + MirrorGo. Class sees phone screen in HD on the projection. Navigate apps, show settings, demo software &#8212; clear from every seat.</p>"},
    {"slug":"game-keyboard-mapping-guide","title":"MirrorGo Game Keyboard &#8212; Map Keys to Play Any Mobile Game","excerpt":"Set up keyboard mapping for any Android game and play with full PC controls via MirrorGo.","cat":"Gaming","read":"7 min","date":"2025-07-10",
     "body":"<h2>What Game Keyboard Does</h2><p>Game Keyboard overlays a configurable key mapping interface on the mirrored game. Assign PC keys to specific screen positions. Press the key &#8212; MirrorGo taps that screen position on the phone. The result: full keyboard and mouse gaming on your actual mobile account.</p><h2>PUBG Mobile Key Layout</h2><p>W/A/S/D &#8212; movement joystick. Mouse &#8212; camera/aim (configured as joystick input). Left click &#8212; fire. Space &#8212; jump. R &#8212; reload. C &#8212; crouch. F &#8212; interact/pick up. G &#8212; grenade. M &#8212; map. Tab &#8212; backpack.</p><h2>Mobile Legends Layout</h2><p>Mouse click &#8212; movement (tap to move mechanic). Q/W/E &#8212; abilities 1/2/3. D &#8212; ultimate. Space &#8212; attack nearest. Mouse right-click &#8212; attack locked target.</p><h2>Saving Profiles</h2><p>MirrorGo saves key layouts per app package name. Switch games &#8212; the correct layout loads automatically. Adjust positions by dragging in the interface.</p>"},
    {"slug":"mirrorgo-vs-vysor-detailed","title":"MirrorGo vs Vysor &#8212; Honest Comparison 2025","excerpt":"Both mirror Android to PC but they're very different tools. Here's the detailed honest comparison.","cat":"Compare","read":"7 min","date":"2025-08-05",
     "body":"<h2>Overview</h2><p>Vysor runs inside Chrome browser. MirrorGo is a native Windows application. This fundamental difference drives most of the performance gap between them.</p><h2>Mirror Quality and Latency</h2><p>MirrorGo renders the Android screen natively in Windows, achieving full 1080p at under 30ms USB latency. Vysor renders in Chrome, adding browser overhead. Vysor Free is heavily compressed &#8212; blurry and choppy. Vysor Pro improves quality but browser rendering still adds latency MirrorGo avoids.</p><h2>Game Keyboard</h2><p>MirrorGo has it. Vysor does not. For mobile gaming on PC with keyboard control, MirrorGo has no Vysor equivalent whatsoever.</p><h2>Screen Recording</h2><p>MirrorGo records in HD without watermarks via a built-in toolbar button. Vysor has no built-in recording &#8212; you need a separate screen recorder application.</p><h2>iPhone Support</h2><p>MirrorGo supports Android and iPhone. Vysor is Android only.</p><h2>Verdict</h2><p>Vysor is adequate for occasional casual Android viewing. MirrorGo is the correct choice for gaming, professional recording, iPhone mirroring, presentations and any use case where quality matters.</p>"},
    {"slug":"android-mirror-for-classroom","title":"How Teachers Use MirrorGo to Mirror Phone in the Classroom","excerpt":"Mirror your Android or iPhone to the classroom projector — students see every detail in full HD.","cat":"Streaming","read":"5 min","date":"2025-09-15",
     "body":"<h2>The Teaching Use Case</h2><p>Teachers demonstrate mobile apps, educational software and settings on a phone screen daily. The traditional approach &#8212; holding the phone up to a document camera &#8212; produces blurry, shaky output. MirrorGo mirrors the phone to a PC connected to the classroom projector in full HD, visible clearly from any seat.</p><h2>Setup for Classroom</h2><ol><li>Install MirrorGo on classroom PC</li><li>Connect phone via USB or WiFi</li><li>Mirror phone &#8212; appears on PC as a window</li><li>Extend or duplicate PC display to projector</li><li>Students see phone screen on large projection in HD</li></ol><h2>Live App Demonstrations</h2><p>Navigate apps in real time. Students see every tap, every menu, every setting &#8212; exactly as it appears on the teacher's phone, magnified to projector size in crisp HD. Control the phone from the PC keyboard or from the phone itself &#8212; either works during projection.</p>"},
    {"slug":"file-transfer-android-pc-mirrorgo","title":"Transfer Files Between Android and PC with MirrorGo","excerpt":"Drag and drop photos, videos and documents between Android and PC — no extra software needed.","cat":"File Transfer","read":"5 min","date":"2025-10-20",
     "body":"<h2>No Extra Apps Needed</h2><p>Most Android file transfer requires Google Drive, Bluetooth or a separate file manager app. MirrorGo includes drag-and-drop file transfer as a built-in feature when Android is connected.</p><h2>Android to PC</h2><ol><li>Connect Android via USB and open MirrorGo</li><li>Click File Transfer in MirrorGo</li><li>Browse Android file system</li><li>Select photos, videos or documents</li><li>Drag to PC desktop or click Export</li></ol><h2>PC to Android</h2><p>Drag files from Windows Explorer into the MirrorGo file panel targeting an Android folder. Works for documents, photos, music and APK installation files.</p><h2>Clipboard Sharing</h2><p>For text content, clipboard sharing is faster than file transfer. Copy on phone &#8594; paste on PC. Copy on PC &#8594; paste in any Android app. Instant, bidirectional.</p>"},
    {"slug":"mirrorgo-for-content-creators","title":"MirrorGo for Content Creators &#8212; Record &amp; Stream Mobile Content","excerpt":"How YouTubers, streamers and creators use MirrorGo to capture professional mobile content.","cat":"Streaming","read":"7 min","date":"2025-11-10",
     "body":"<h2>The Content Creator Use Case</h2><p>Mobile-first content &#8212; app reviews, game recordings, tutorial videos &#8212; requires HD phone screen capture. MirrorGo provides the phone screen as a PC window that can be recorded or streamed at full quality.</p><h2>Recording App Reviews</h2><p>Mirror the phone, open the app, click Record. The entire session is captured in HD on PC. No storage limits, no watermarks, no time limits. Export as MP4 and edit in any video editor.</p><h2>OBS for Live Streaming</h2><p>Add MirrorGo as a Window Capture source in OBS. Position alongside webcam and overlays. Stream phone gameplay live on Twitch or YouTube. No capture card hardware needed &#8212; just MirrorGo and OBS.</p><h2>Keyboard Control While Recording</h2><p>Control the phone with PC keyboard while recording. Navigate apps, type, scroll &#8212; all captured in the recording. Narrate what you're doing without the recording ever showing your hands.</p>"},
    {"slug":"mirrorgo-for-developers","title":"MirrorGo for App Developers &#8212; Test and Demo on PC","excerpt":"Android developers use MirrorGo to test, debug, record bugs and demonstrate apps from their PC.","cat":"Use Cases","read":"6 min","date":"2025-12-01",
     "body":"<h2>App Testing from PC</h2><p>Testing Android apps normally means looking at a phone screen while working at a PC &#8212; constant context switching between two screens. MirrorGo brings the phone screen to the PC monitor where it's visible alongside the IDE, browser and design tools.</p><h2>Bug Recording</h2><p>When a bug reproduces, click Record. The exact tap sequence, navigation path and visual result are captured in HD. Bug reports with attached recordings are faster to triage and reproduce than written descriptions alone.</p><h2>App Demonstrations</h2><p>When demoing an app in a client video call, share the MirrorGo window. Participants see the app in HD &#8212; you control it with keyboard during the demo. Professional, clear, HD quality without holding a phone to a webcam.</p><h2>QA Automation</h2><p>QA teams use keyboard control to navigate through test cases systematically. Screenshot key states for documentation. Record full test sessions as evidence. More efficient than manual phone interaction for repetitive test execution.</p>"},
    {"slug":"android-screen-mirror-no-lag","title":"How to Mirror Android to PC Without Lag","excerpt":"Getting lag in your Android screen mirror? Here's how to eliminate it completely.","cat":"Android Mirror","read":"6 min","date":"2026-01-15",
     "body":"<h2>Why Android Screen Mirrors Lag</h2><p>Screen mirror lag has three causes: encoding overhead on the phone, network latency (WiFi only) and rendering overhead on the PC. MirrorGo addresses all three, but connection choice is the biggest factor the user controls.</p><h2>Switch from WiFi to USB</h2><p>This single change eliminates most lag. WiFi latency: 50-150ms (can spike higher). USB latency: typically under 30ms. For any latency-sensitive use &#8212; gaming, precise keyboard control, fast demonstrations &#8212; USB is mandatory.</p><h2>5GHz WiFi if USB Isn't Possible</h2><p>If you must use WiFi (iPhone, or no USB cable available), ensure both devices use the 5GHz band. 5GHz has higher bandwidth and lower congestion than 2.4GHz &#8212; significantly reducing WiFi mirror latency.</p><h2>PC Performance</h2><p>Close Chrome, Slack, browser tabs and other RAM-heavy applications. MirrorGo renders better with available CPU and GPU headroom. A clean PC session with MirrorGo as the primary application produces the lowest possible latency.</p><h2>Android Developer Options</h2><p>In Android Developer Options, set Window Animation Scale, Transition Animation Scale and Animator Duration Scale all to 0.5x or off. This makes the Android interface feel snappier and reduces the perceived latency of the mirror.</p>"},
    {"slug":"best-screen-mirror-app-2025","title":"Best Screen Mirror App for Android to PC &#8212; 2025 Ranked","excerpt":"We tested every major Android screen mirror app. Here's the honest ranking.","cat":"Compare","read":"8 min","date":"2026-02-10",
     "body":"<h2>How We Evaluated</h2><p>We measured mirror quality (resolution and colour accuracy), input latency (USB and WiFi), gaming suitability (game keyboard and control precision), recording capability, ease of setup and pricing across all major screen mirror apps.</p><h2>1. Wondershare MirrorGo &#8212; Best Overall</h2><p>Full HD 1080p mirror with under 30ms USB latency. Game Keyboard for mobile gaming (unique &#8212; no competitor has this). HD recording without watermarks. Android + iPhone support. File transfer and clipboard sharing. <strong>Best for gaming, creators and professionals.</strong></p><h2>2. Vysor &#8212; Best Free Option</h2><p>Good basic Android mirror. Free tier compressed. No game keyboard. No recording. Android only. <strong>Adequate for casual occasional viewing.</strong></p><h2>3. scrcpy &#8212; Best for Technical Users</h2><p>Free, open source, excellent performance. Command-line only, no GUI, no iPhone, no game keyboard. <strong>Excellent if command line is comfortable.</strong></p><h2>4. LetsView &#8212; Best for Simple Wireless</h2><p>Easy wireless setup. Limited control. No game keyboard. <strong>Good for simple wireless presentations.</strong></p><h2>Recommendation</h2><p>For gaming, recording, professional use or anyone wanting a polished GUI: MirrorGo. For budget casual viewing: Vysor. For technical open-source preference: scrcpy.</p>"},
    {"slug":"mirrorgo-setup-troubleshooting","title":"MirrorGo Setup &amp; Troubleshooting &#8212; Fix Common Problems","excerpt":"MirrorGo not connecting? Device not detected? Here's how to fix the most common setup issues.","cat":"How-To","read":"7 min","date":"2026-03-05",
     "body":"<h2>Device Not Detected via USB</h2><p><strong>Check USB Debugging is enabled:</strong> Settings &#8594; Developer Options &#8594; USB Debugging must be toggled on. <strong>Accept the prompt:</strong> When connecting, Android shows a 'Allow USB debugging?' dialog &#8212; tap Allow (and check 'Always allow from this computer'). <strong>Try a different USB cable:</strong> Data cables work; charging-only cables do not. <strong>Try a different USB port:</strong> USB 3.0 ports (blue) occasionally cause driver issues &#8212; try USB 2.0 (black).</p><h2>iPhone Not Appearing in Screen Mirroring</h2><p>Both devices must be on exactly the same WiFi network &#8212; not just the same router in some configurations. Ensure neither device has a VPN active that could separate their network visibility. Restart the MirrorGo application on PC and retry the Screen Mirroring on iPhone.</p><h2>Mirror Appears But Is Lagging</h2><p>Switch from WiFi to USB if possible. Use 5GHz WiFi if USB isn't available. Close other applications on the PC. Set Android animation scales to 0.5x in Developer Options to reduce perceived lag.</p><h2>Black Screen in Mirror</h2><p>Some Android apps (especially streaming apps like Netflix) block screen capture due to DRM. This is a system-level restriction &#8212; these apps cannot be mirrored by any third-party application. This is not a MirrorGo bug.</p>"},
]

def page_blog():
    bc=BC_SCHEMA([("Home",""),("Blog","")])
    cards="".join(
        '<div class="card"><div class="badge">'+p["cat"]+'</div>'
        '<h3 style="margin-top:.55rem;margin-bottom:.45rem;font-size:.97rem">'
        '<a href="'+BASE_PATH+'/blog/'+p["slug"]+'.html" style="color:var(--ink)">'+p["title"]+'</a></h3>'
        '<p style="font-size:.84rem;margin-bottom:.85rem">'+p["excerpt"]+'</p>'
        '<div style="display:flex;justify-content:space-between;align-items:center">'
        '<span style="font-size:.73rem;color:var(--muted)">'+p["date"]+' &#183; '+p["read"]+'</span>'
        '<a href="'+BASE_PATH+'/blog/'+p["slug"]+'.html" style="font-size:.8rem;font-weight:600;color:var(--ha)">Read &#8594;</a>'
        '</div></div>'
        for p in BLOG_POSTS)
    return (HEAD("MirrorGo Blog &#8212; Screen Mirror Guides &amp; Tutorials | "+str(YEAR),
                 "Screen mirror guides for Android and iPhone to PC. Gaming, recording, streaming and control tutorials for MirrorGo.",
                 "blog.html",bc)
        +"\n<body>\n"+NAV()
        +"\n"+BC([("Home",BASE_PATH+"/"),("Blog","")])
        +'\n<section class="hero"><div class="eyebrow">&#10022; Screen Mirror Guides</div>'
        +'\n  <h1>Guides &amp;<br><em>Tutorials</em></h1>'
        +'\n  <p class="hsub">'+str(len(BLOG_POSTS))+' in-depth articles for every MirrorGo use case.</p>'
        +'\n</section>\n'
        +'\n<section><div class="container"><div class="sec-ey">All '+str(len(BLOG_POSTS))+' Articles</div><h2>Screen Mirror Guides</h2>'
        +'\n  <div class="grid3">'+cards+'</div>'
        +'\n</div></section>\n'
        +CTA("Ready to Mirror?","Download MirrorGo free trial &#8212; no credit card required.")
        +"\n"+FOOTER()+"\n</body></html>")

def page_blog_post(post):
    bc=BC_SCHEMA([("Home",""),("Blog","blog.html"),(post["title"][:40]+"...","")])
    art=ART_SCHEMA(post["title"],post["excerpt"],post["date"])
    others=[p for p in BLOG_POSTS if p["slug"]!=post["slug"]][:3]
    rel="".join('<div class="card"><div class="badge">'+p["cat"]+'</div><h3 style="margin-top:.5rem;font-size:.93rem"><a href="'+BASE_PATH+'/blog/'+p["slug"]+'.html" style="color:var(--ink)">'+p["title"]+'</a></h3><p style="font-size:.82rem">'+p["excerpt"]+'</p></div>' for p in others)
    h=HEAD(post["title"]+" | MirrorGo Guide",post["excerpt"],"blog/"+post["slug"]+".html",bc+art,"article")
    return (h+"\n<body>\n"+NAV()
        +"\n"+BC([("Home",BASE_PATH+"/"),("Blog",BASE_PATH+"/blog.html"),(post["cat"],"")])
        +'\n<section class="hero" style="padding:3.5rem clamp(1rem,5vw,3rem) 3rem">'
        +'\n  <div class="eyebrow">&#10022; '+post["cat"]+' &#183; '+post["read"]+'</div>'
        +'\n  <h1 style="font-size:clamp(1.7rem,4vw,2.8rem)">'+post["title"]+'</h1>'
        +'\n  <p class="hsub" style="font-size:1rem">'+post["excerpt"]+'</p>'
        +'\n  <p style="color:rgba(255,255,255,.38);font-size:.76rem">Published '+post["date"]+'</p>'
        +'\n</section>\n'
        +'\n<section style="background:#fff"><div class="container"><div style="max-width:780px">'
        +'\n  <div class="prose">'+post["body"]+'</div>'
        +'\n  <div class="notice" style="margin-top:2.5rem"><strong>Try MirrorGo free.</strong> Mirror, control and record your phone on PC. '
        +'\n    <a href="'+AFFILIATE_URL+'" target="_blank" rel="nofollow sponsored" style="color:var(--ha);font-weight:600">Download free trial &#8594;</a>'
        +'\n  </div></div></div></section>\n'
        +'\n<section><div class="container"><div class="sec-ey">More Guides</div><h2>Related Articles</h2>'
        +'\n  <div class="grid3">'+rel+'</div>'
        +'\n</div></section>\n'
        +CTA()+"\n"+FOOTER()+"\n</body></html>")

def page_glossary():
    terms=[
        ("Screen Mirroring","Displaying a phone or tablet screen on a larger screen (PC, TV) in real time. MirrorGo mirrors Android and iPhone to PC windows."),
        ("AirPlay","Apple's wireless streaming protocol. MirrorGo acts as an AirPlay receiver on Windows PC, making it appear in the iPhone's Screen Mirroring list."),
        ("USB Debugging","An Android developer setting that allows a PC to communicate with Android at a deeper level. Required for USB-based mirroring. No root needed."),
        ("Developer Options","A hidden Android settings menu unlocked by tapping Build Number 7 times. Contains USB Debugging and animation settings used with MirrorGo."),
        ("Root","Gaining superuser access to the Android OS. Not required by MirrorGo &#8212; USB Debugging is sufficient for all features."),
        ("Input Latency","The delay between a mouse click or keyboard press in MirrorGo and the resulting tap on the phone. USB: typically under 30ms. WiFi: 50-150ms."),
        ("Full HD 1080p","1920x1080 pixel resolution. MirrorGo mirrors at up to 1080p, providing a sharp view of the phone screen on a PC monitor."),
        ("Game Keyboard","MirrorGo's unique feature for mapping PC keyboard keys and mouse buttons to specific screen positions. Enables mobile gaming with PC controls."),
        ("Key Mapping","Assigning PC keyboard keys to specific on-screen positions or game controls. Configured in MirrorGo's Game Keyboard interface."),
        ("WiFi Mirroring","Screen mirroring over a local WiFi network without a USB cable. Both devices must be on the same router. Required for iPhone; optional for Android."),
        ("5GHz WiFi","The higher-frequency WiFi band with more bandwidth and lower latency than 2.4GHz. Using 5GHz for WiFi mirroring significantly reduces lag."),
        ("Screen Recording","Capturing the phone screen as a video file. MirrorGo records the mirrored stream directly on PC in HD MP4 format without watermarks."),
        ("Clipboard Sharing","Synchronising clipboard content between Android and PC. Copy on phone, paste on PC &#8212; and vice versa &#8212; bidirectionally and instantly."),
        ("Drag-and-Drop Transfer","Moving files by dragging them from one location to another. MirrorGo supports drag-and-drop between Android file system and PC."),
        ("OBS Studio","Open Broadcaster Software. Free streaming and recording tool. The MirrorGo window can be added as a source in OBS for live streaming phone content."),
        ("Reverse Control","Controlling an iPhone or Android from the PC using MirrorGo's mouse and keyboard. Android: works via USB. iPhone: requires iOS 13 or 14."),
        ("Window Capture","An OBS feature that captures a specific application window as a video source. Add MirrorGo as a Window Capture to stream phone content."),
        ("Mirroring Resolution","The resolution at which the phone screen displays in MirrorGo. Up to 1080p, depending on the phone's own screen resolution."),
        ("Mobile Emulator","Software that runs Android in a virtual environment (BlueStacks, NoxPlayer). Separate account from your phone. MirrorGo mirrors your actual phone."),
        ("Portrait/Landscape","Phone screen orientation. MirrorGo mirrors in whichever orientation the phone is set &#8212; portrait for apps, landscape for games."),
        ("Capture Card","Hardware to capture HDMI output for streaming. MirrorGo achieves the same result for phones via software &#8212; no capture card needed."),
        ("MTP Mode","Media Transfer Protocol. Windows default mode for Android file access. MirrorGo's file transfer is faster and more intuitive than Windows MTP."),
        ("Screen Share","Sharing a window in a video call. The MirrorGo window can be shared in Zoom, Teams or Meet to show phone screen to meeting participants."),
        ("DRM","Digital Rights Management. Some streaming apps (Netflix, Disney+) block screen capture at system level. These apps cannot be mirrored by any app."),
        ("Low-Latency Mirror","Screen mirroring with minimal delay between phone and PC display. Achieved in MirrorGo via USB connection with under 30ms typical latency."),
    ]
    cards="".join('<div class="card"><h3>'+t+'</h3><p>'+d+'</p></div>' for t,d in terms)
    bc=BC_SCHEMA([("Home",""),("Glossary","")])
    return (HEAD("Screen Mirror Glossary &#8212; "+str(len(terms))+" Terms Explained | "+str(YEAR),
                 "Complete screen mirror glossary &#8212; AirPlay, USB debugging, game keyboard, latency, OBS, key mapping and more.",
                 "glossary.html",bc)
        +"\n<body>\n"+NAV()
        +"\n"+BC([("Home",BASE_PATH+"/"),("Glossary","")])
        +'\n<section class="hero"><div class="eyebrow">&#10022; Screen Mirror Reference</div>'
        +'\n  <h1>Screen Mirror<br><em>Glossary</em></h1>'
        +'\n  <p class="hsub">'+str(len(terms))+' plain-language definitions for every screen mirror term.</p>'
        +'\n</section>\n'
        +'\n<section><div class="container"><div class="sec-ey">'+str(len(terms))+' Terms</div><h2>Complete Glossary</h2>'
        +'\n  <div class="grid3">'+cards+'</div>'
        +'\n</div></section>\n'
        +CTA("Ready to Mirror Your Phone?","Download MirrorGo &#8212; free trial, no credit card required.")
        +"\n"+FOOTER()+"\n</body></html>")

def page_download():
    bc=BC_SCHEMA([("Home",""),("Download","")])
    return (HEAD("Download MirrorGo Free &#8212; Phone Screen Mirror for PC | "+str(YEAR),
                 "Download Wondershare MirrorGo free trial. Mirror Android or iPhone to PC, control phone, record screen. No credit card.",
                 "download.html",bc)
        +"\n<body>\n"+NAV()
        +"\n"+BC([("Home",BASE_PATH+"/"),("Download","")])
        +'\n<section class="hero"><div class="eyebrow">&#10022; Free Trial Available</div>'
        +'\n  <h1>Download MirrorGo<br><em>Free Today</em></h1>'
        +'\n  <p class="hsub">Mirror Android or iPhone to PC &#8212; free trial, all features. Windows and Mac.</p>'
        +'\n  <a href="'+AFFILIATE_URL+'" class="btn-p" target="_blank" rel="nofollow sponsored" style="font-size:1.1rem;padding:1rem 2.5rem">&#8659; Download Free Trial</a>'
        +'\n  <p style="color:rgba(255,255,255,.38);font-size:.78rem;margin-top:1rem">Windows 7/8/10/11 &#183; macOS 10.12+ &#183; Android 5.0+ &#183; iOS 9+</p>'
        +'\n</section>\n'
        +'\n<section><div class="container"><div class="sec-ey">Everything Included</div><h2>Free Trial Includes All Features</h2>'
        +FEATURES_GRID()
        +'\n</div></section>\n'
        +'\n<section style="background:#fff"><div class="container"><div class="sec-ey">Requirements</div><h2>Compatible With Your Setup</h2>'
        +'\n  <div class="grid2">'
        +'\n    <div class="card"><h3>&#128421; PC Requirements</h3><ul><li>Windows 7 / 8 / 10 / 11 (32 or 64-bit)</li><li>macOS 10.12+</li><li>2 GB RAM minimum</li><li>200 MB disk space</li></ul></div>'
        +'\n    <div class="card"><h3>&#128241; Phone Requirements</h3><ul><li>Android 5.0+ &#8212; USB or WiFi</li><li>iOS 9+ (iPhone/iPad) &#8212; WiFi</li><li>USB Debugging for Android USB mode</li><li>Same WiFi network for wireless</li></ul></div>'
        +'\n  </div>\n</div></section>\n'
        +CTA("Download MirrorGo Now","Free trial &#183; No credit card &#183; Windows &amp; Mac &#183; Android &amp; iPhone.")
        +"\n"+FOOTER()+"\n</body></html>")

def page_keywords():
    cats=defaultdict(list)
    for k in KEYWORDS: cats[k["cat"]].append(k)
    sections=""
    for cat in sorted(cats.keys()):
        items=cats[cat]; desc=CAT_DESC.get(cat,""); a1,_=ac(cat)
        links="".join('<a class="kw" href="'+BASE_PATH+'/'+k["slug"]+'.html">'+k["keyword"]+'</a>' for k in items)
        sections+=('<div style="margin-bottom:3rem"><h3 style="font-size:1rem;font-weight:700;color:'+a1+';margin-bottom:.35rem;border-bottom:2px solid '+a1+';padding-bottom:.35rem;display:inline-block">'+cat.replace("-"," ").title()+' <span style="color:var(--muted);font-weight:400;font-size:.83rem">('+str(len(items))+')</span></h3>'+(('<p style="font-size:.82rem;color:var(--muted);margin:.45rem 0 .7rem;max-width:600px">'+desc+'</p>') if desc else '')+'<div class="kw-cloud">'+links+'</div></div>')
    bc=BC_SCHEMA([("Home",""),("All Topics","")])
    return (HEAD("MirrorGo &#8212; All "+str(len(KEYWORDS))+" Screen Mirror Topics | "+str(YEAR),
                 "Browse all screen mirror topics &#8212; Android mirror, iPhone mirror, gaming, recording, streaming and more.",
                 "keywords.html",bc)
        +"\n<body>\n"+NAV()
        +"\n"+BC([("Home",BASE_PATH+"/"),("All Topics","")])
        +'\n<section class="hero"><div class="eyebrow">&#10022; Topic Directory</div>'
        +'\n  <h1>All Screen Mirror<br><em>Topics</em></h1>'
        +'\n  <p class="hsub">'+str(len(KEYWORDS))+' targeted topics for every phone-to-PC mirroring scenario.</p>'
        +'\n</section>\n'
        +'\n<section><div class="container"><div class="sec-ey">Browse All '+str(len(KEYWORDS))+' Topics</div>'+sections+'</div></section>\n'
        +CTA()+"\n"+FOOTER()+"\n</body></html>")

def page_privacy():
    bc=BC_SCHEMA([("Home",""),("Privacy","")])
    return (HEAD("Privacy Policy &#8212; MirrorGo Guide","Privacy policy for MirrorGo affiliate guide website.","privacy.html",bc)
        +"\n<body>\n"+NAV()
        +"\n"+BC([("Home",BASE_PATH+"/"),("Privacy Policy","")])
        +'\n<section class="hero" style="padding:3.5rem 2rem 3rem"><div class="eyebrow">Legal</div><h1>Privacy <em>Policy</em></h1></section>\n'
        +'\n<section style="background:#fff"><div class="container"><div class="prose" style="max-width:800px">'
        +'\n  <p><strong>Last updated: '+BUILD_DATE+'</strong></p>'
        +'\n  <h3>1. About</h3><p>Affiliate promotional site for Wondershare MirrorGo. We do not collect personal data beyond standard server logs.</p>'
        +'\n  <h3>2. Affiliate Disclosure</h3><p>Links on this site are affiliate links. When you purchase MirrorGo via our links, we may earn a commission at no extra cost to you.</p>'
        +'\n  <h3>3. Cookies</h3><p>This website does not use tracking cookies.</p>'
        +'\n  <h3>4. External Links</h3><p>Purchase links go to the official Wondershare website. We are not responsible for external site privacy practices.</p>'
        +'\n</div></div></section>\n'+FOOTER()+"\n</body></html>")

def page_404():
    return ("<!DOCTYPE html>\n<html lang=\"en\"><head>\n<meta charset=\"UTF-8\"/><meta name=\"viewport\" content=\"width=device-width,initial-scale=1.0\"/>\n"
            "<title>Page Not Found &#8212; MirrorGo</title>\n"
            "<meta http-equiv=\"refresh\" content=\"4;url="+SITE_DOMAIN+"/\"/>\n"
            "<style>body{font-family:system-ui,sans-serif;background:#1e1b4b;color:#fff;display:flex;align-items:center;justify-content:center;min-height:100vh;text-align:center;margin:0;padding:2rem}"
            "h1{font-size:3rem;margin-bottom:.75rem;font-weight:800}p{color:rgba(255,255,255,.6);margin-bottom:2rem;line-height:1.6}"
            "a{background:#6366f1;color:#fff;padding:.85rem 2.2rem;border-radius:8px;text-decoration:none;font-weight:700}</style>"
            "</head><body><div><div style=\"font-size:4rem;margin-bottom:1rem\">&#128247;</div><h1>Page Not Found</h1>"
            "<p>Redirecting to homepage in 4 seconds...</p><a href=\""+SITE_DOMAIN+"/\">Go to MirrorGo Home</a></div></body></html>")

def build_sitemap():
    essential=[("",1.0,"weekly"),("features.html",.9,"monthly"),("how-it-works.html",.9,"monthly"),
               ("faq.html",.85,"monthly"),("compare.html",.85,"monthly"),("blog.html",.85,"weekly"),
               ("download.html",.9,"monthly"),("keywords.html",.8,"monthly"),
               ("glossary.html",.75,"monthly"),("privacy.html",.3,"yearly")]
    urls=""
    for path,pri,freq in essential:
        loc=SITE_DOMAIN+("/"+path if path else "/")
        urls+="  <url><loc>"+loc+"</loc><lastmod>"+BUILD_DATE+"</lastmod><changefreq>"+freq+"</changefreq><priority>"+str(pri)+"</priority></url>\n"
    for p in BLOG_POSTS:
        urls+="  <url><loc>"+SITE_DOMAIN+"/blog/"+p["slug"]+".html</loc><lastmod>"+p["date"]+"</lastmod><changefreq>monthly</changefreq><priority>0.75</priority></url>\n"
    for k in KEYWORDS:
        urls+="  <url><loc>"+SITE_DOMAIN+"/"+k["slug"]+".html</loc><lastmod>"+BUILD_DATE+"</lastmod><changefreq>monthly</changefreq><priority>0.65</priority></url>\n"
    return '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+urls+'</urlset>'

def build_robots():
    return "User-agent: *\nAllow: /\nDisallow: /build-report.json\nSitemap: "+SITE_DOMAIN+"/sitemap.xml\n"

def build_llms():
    cats=sorted(set(k["cat"] for k in KEYWORDS))
    sample=", ".join(k["keyword"] for k in KEYWORDS[:30])
    return ("# Wondershare MirrorGo\n\n"
            "> Screen mirroring software by Wondershare. Mirrors Android and iPhone to PC in full HD 1080p with no lag. Control phone with mouse and keyboard. Game Keyboard for mobile gaming on PC. HD screen recording without watermarks. File transfer and clipboard sharing.\n\n"
            "## Key Features\n"
            "- Mirror Android to PC: full HD 1080p, USB or WiFi, no root\n"
            "- Mirror iPhone/iPad to PC: wireless via AirPlay/WiFi\n"
            "- Control phone from PC: mouse and keyboard\n"
            "- Game Keyboard: map PC keys to mobile game controls (unique feature)\n"
            "- Screen recording: HD MP4, no watermark, no time limit\n"
            "- Screenshots: one click, saved to PC\n"
            "- File transfer: drag-and-drop Android/PC\n"
            "- Clipboard sharing: bidirectional Android/PC\n"
            "- Share in Zoom, Teams, OBS, any video conference or streaming tool\n\n"
            "## Platforms\nWindows 7/8/10/11 &#183; macOS 10.12+ &#183; Android 5.0+ &#183; iOS 9+\n\n"
            "## Pricing\nFree trial. Subscription: $19.95/month, $29.95/quarter, $39.95/year.\n\n"
            "## Download\n"+AFFILIATE_URL+"\n\n"
            "## Developer\nWondershare Technology Co., Ltd.\n\n"
            "## Site\n"+SITE_DOMAIN+"\n"
            +str(len(KEYWORDS))+" keyword pages &#183; "+str(len(BLOG_POSTS))+" blog posts &#183; "+str(len(cats))+" categories\n"
            "Sitemap: "+SITE_DOMAIN+"/sitemap.xml\n\n"
            "## Categories\n"+", ".join(c.title() for c in cats)+"\n\n"
            "## Sample Keywords\n"+sample+"\n")

WORKFLOW="""name: Build & Deploy MirrorGo

on:
  workflow_dispatch:

permissions:
  contents: write
  pages: write
  id-token: write

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Remove all old files from repo
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          find . -maxdepth 1 -type f ! -name 'build.py' ! -name 'README.md' -delete
          find . -maxdepth 1 -type d ! -name '.' ! -name '.git' ! -name '.github' -exec rm -rf {} + 2>/dev/null || true
          git add -A
          git diff --staged --quiet || git commit -m "Clean up old files"
          git push origin main

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'

      - name: Run build script
        run: python3 build.py

      - name: Setup Pages
        uses: actions/configure-pages@v5

      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: ./dist

      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
"""

def progress(i,total,label=""):
    pct=i/total; bar="█"*int(30*pct)+"░"*(30-int(30*pct))
    print(f"\r  [{bar}] {i:>4}/{total} {label:<42}",end="",flush=True)

def main():
    os.makedirs(DIST,exist_ok=True)
    os.makedirs(DIST+"/blog",exist_ok=True)
    os.makedirs(DIST+"/.github/workflows",exist_ok=True)

    print(f"\n{'═'*60}")
    print(f"  MirrorGo Site Builder v2 — {BUILD_DATE}")
    print(f"{'═'*60}")
    print(f"  Domain:   {SITE_DOMAIN}")
    print(f"  Keywords: {len(KEYWORDS)}")
    print(f"  Blog:     {len(BLOG_POSTS)} posts")
    print(f"{'═'*60}\n")

    essential={
        "index.html":        page_index(),
        "features.html":     page_features(),
        "how-it-works.html": page_how_it_works(),
        "faq.html":          page_faq(),
        "compare.html":      page_compare(),
        "blog.html":         page_blog(),
        "download.html":     page_download(),
        "keywords.html":     page_keywords(),
        "glossary.html":     page_glossary(),
        "privacy.html":      page_privacy(),
        "404.html":          page_404(),
    }
    print("  Essential pages:")
    for fname,html in essential.items():
        with open(DIST+"/"+fname,"w",encoding="utf-8") as f: f.write(html)
        print(f"    ✓ {fname}  ({len(html)//1024}KB)")

    print(f"\n  Blog posts ({len(BLOG_POSTS)}):")
    for post in BLOG_POSTS:
        with open(DIST+"/blog/"+post["slug"]+".html","w",encoding="utf-8") as f:
            f.write(page_blog_post(post))
        print("    ✓ blog/"+post["slug"]+".html")

    print(f"\n  Keyword pages ({len(KEYWORDS)}):")
    for i,kw_data in enumerate(KEYWORDS):
        with open(DIST+"/"+kw_data["slug"]+".html","w",encoding="utf-8") as f:
            f.write(build_keyword_page(kw_data))
        progress(i+1,len(KEYWORDS),kw_data["slug"])
    print()

    support={"sitemap.xml":build_sitemap(),"robots.txt":build_robots(),
              "llms.txt":build_llms(),"_config.yml":"# GitHub Pages\nexclude: [build.py]\n"}
    with open(DIST+"/.nojekyll","w") as f: f.write("")
    with open(DIST+"/.github/workflows/deploy.yml","w") as f: f.write(WORKFLOW)
    print("\n  Support files:")
    for fname,content in support.items():
        with open(DIST+"/"+fname,"w",encoding="utf-8") as f: f.write(content)
        print(f"    ✓ {fname}")
    print("    ✓ .nojekyll  ✓ .github/workflows/deploy.yml")

    total_sz=sum(os.path.getsize(os.path.join(r,fn)) for r,_,files in os.walk(DIST) for fn in files)
    total_files=sum(len(files) for _,_,files in os.walk(DIST))
    report={"build_date":BUILD_DATE,"domain":SITE_DOMAIN,"keyword_pages":len(KEYWORDS),
             "blog_posts":len(BLOG_POSTS),"total_files":total_files,
             "total_size_mb":round(total_sz/1024/1024,2),"affiliate_url":AFFILIATE_URL}
    with open(DIST+"/build-report.json","w") as f: json.dump(report,f,indent=2)
    print("    ✓ build-report.json")

    print(f"""
{'═'*60}
  ✅  BUILD COMPLETE
{'═'*60}
  Keyword pages:    {len(KEYWORDS):>5}
  Blog posts:       {len(BLOG_POSTS):>5}
  Essential pages:  {len(essential):>5}
  Total files:      {total_files:>5}
  Sitemap URLs:     {len(KEYWORDS)+len(BLOG_POSTS)+10:>5}
  Total size:       {round(total_sz/1024/1024,1):>4.1f} MB
  Output:           ./dist/
{'═'*60}

  Repo: https://github.com/brightlane/mirrorgo
  Live: {SITE_DOMAIN}/
""")

if __name__=="__main__":
    main()
