$ErrorActionPreference = 'Stop'
$assetDir = Join-Path $PSScriptRoot '../assets'
function Frame($title, $height, $body) {
@"
<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="$height" viewBox="0 0 1000 $height" role="img" aria-label="$title">
<title>$title</title>
<defs><linearGradient id="shell" x2="1" y2="1"><stop stop-color="#52665d"/><stop offset="1" stop-color="#172820"/></linearGradient><pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse"><path d="M32 0H0V32" fill="none" stroke="#173025" stroke-width=".5"/></pattern></defs>
<style>text{font-family:Consolas,monospace;fill:#e8f5ee}.muted{fill:#9abbab}.mint{fill:#3dffa0}.head{animation:tilt 8s ease-in-out infinite;transform-box:fill-box;transform-origin:center}.eyes{animation:blink 5s infinite;transform-box:fill-box;transform-origin:center}.dot{animation:pulse 1.8s infinite}.flow{stroke-dasharray:6 10;animation:flow 5s linear infinite}@keyframes tilt{0%,35%,100%{transform:rotate(0deg)}55%,75%{transform:rotate(9deg)}}@keyframes blink{0%,90%,96%,100%{transform:scaleY(1)}93%{transform:scaleY(.12)}}@keyframes pulse{0%,100%{opacity:.2}50%{opacity:1}}@keyframes flow{to{stroke-dashoffset:-80}}@media(prefers-reduced-motion:reduce){.head,.eyes,.dot,.flow{animation:none}}</style>
<rect width="1000" height="$height" rx="20" fill="#080f0d"/><rect width="1000" height="$height" rx="20" fill="url(#grid)"/>
$body
</svg>
"@
}
function Robot($x, $y, $scale) {
@"
<g transform="translate($x $y) scale($scale)">
<ellipse cx="0" cy="185" rx="100" ry="12" fill="#3dffa0" opacity=".08"/>
<rect x="-48" y="55" width="96" height="92" rx="37" fill="url(#shell)" stroke="#789b88" stroke-width="2"/>
<circle cy="87" r="12" fill="#102219" stroke="#3dffa0" stroke-width="3"/>
<path d="M-26 140L-38 170M26 140L40 170" stroke="#41594c" stroke-width="28" stroke-linecap="round"/>
<ellipse cx="-43" cy="176" rx="26" ry="13" fill="#60796b"/><ellipse cx="45" cy="176" rx="26" ry="13" fill="#60796b"/>
<path d="M-45 76Q-87 70 -67 20M46 78L59 125" fill="none" stroke="#526b5d" stroke-width="21" stroke-linecap="round"/>
<g class="head"><rect x="-91" y="-43" width="182" height="106" rx="49" fill="url(#shell)" stroke="#a2b8ac" stroke-width="3"/>
<rect x="-76" y="-30" width="152" height="78" rx="33" fill="#060f0b"/>
<g class="eyes" fill="#6dffbb"><circle cx="-35" cy="9" r="7"/><circle cx="35" cy="9" r="7"/></g></g>
<g fill="#3dffa0"><circle class="dot" cx="100" cy="-40" r="4"/><circle class="dot" style="animation-delay:.3s" cx="116" cy="-40" r="4"/><circle class="dot" style="animation-delay:.6s" cx="132" cy="-40" r="4"/></g></g>
"@
}
function AnimatedHeadline($label, $y, $offset) {
 $letters = ''
 for ($i = 0; $i -lt $label.Length; $i++) {
  $delay = ($offset + $i * .055).ToString('0.000', [System.Globalization.CultureInfo]::InvariantCulture)
  $letter = [System.Security.SecurityElement]::Escape([string]$label[$i])
  $letters += "<tspan class='letter' style='animation-delay:${delay}s'>$letter</tspan>"
 }
 return "<text x='40' y='$y' xml:space='preserve' style='font-family:Georgia,serif' font-size='53'>$letters</text>"
}
$hero = @"
<style>
.letter{animation:letter-in 12s linear infinite;fill:#f1f1e7}
@keyframes letter-in{0%,2%{opacity:0;fill:#3dffa0}5%,89%{opacity:1}94%,100%{opacity:0}}
.status{opacity:0;animation:status-cycle 16s infinite}
.status-two{animation-delay:4s}.status-three{animation-delay:8s}.status-four{animation-delay:12s}
@keyframes status-cycle{0%,22%{opacity:1}25%,100%{opacity:0}}
.cursor{animation:cursor-blink 1s steps(1) infinite}
@keyframes cursor-blink{50%{opacity:0}}
@media(prefers-reduced-motion:reduce){.letter{animation:none;opacity:1}.status{animation:none;opacity:0}.status-one{opacity:1}.cursor{animation:none}}
</style>
<text x="42" y="42" font-size="13" letter-spacing="3" class="mint">PERSONAL ENGINEERING LAB / THINKER × MINDOO</text>
<text x="42" y="100" font-size="20">NGUYEN THANH AN <tspan class="muted">/ thinker</tspan></text>
$(AnimatedHeadline 'Ideas on paper.' 178 0)
$(AnimatedHeadline 'Systems in code.' 240 1.1)
$(AnimatedHeadline 'Worlds in motion.' 302 2.3)
<path d="M42 330H115" stroke="#3dffa0" stroke-width="3"/>
<text x="42" y="369" font-size="16" class="muted">Software · AI · Games · Mathematics</text>
<path d="M665 350H935M680 365H940M670 380H930" stroke="#365747" stroke-width="12"/>
$(Robot 792 150 1.04)
<text x="750" y="420" font-size="18" letter-spacing="4" class="mint">MINDOO</text>
<text x="42" y="425" font-size="14" class="muted">Always a student of the problem.</text>
<path d="M42 453H958" stroke="#244334"/>
<text x="42" y="489" font-size="13" class="mint">MINDOO / FIELD NOTES</text>
<g font-size="14" class="muted">
<text x="280" y="489" class="status status-one">Reading the problem. Questioning the obvious.</text>
<text x="280" y="489" class="status status-two">Thinking on paper. Connecting the dots.</text>
<text x="280" y="489" class="status status-three">Building something small. Testing an idea.</text>
<text x="280" y="489" class="status status-four">A blank stare. A new hypothesis.</text>
</g><rect class="cursor" x="929" y="476" width="8" height="16" fill="#3dffa0"/>
"@
Frame 'THINKER and MINDOO — ideas on paper, systems in code, worlds in motion; animated lettering and field notes' 520 $hero | Set-Content (Join-Path $assetDir 'banner.svg') -Encoding utf8
$meet = @"
$(Robot 160 87 .8)
<text x="325" y="65" font-size="14" letter-spacing="3" class="mint">MEET MINDOO</text>
<text x="325" y="115" font-size="29">A curious companion.</text>
<text x="325" y="155" font-size="29">A thoughtful way to build.</text>
<text x="325" y="205" font-size="15" class="muted">Observe → Reason → Plan → Act → Reflect</text>
<text x="325" y="246" font-size="13" class="mint">The experiment failed. The notebook improved.</text>
"@
Frame 'Meet MINDOO, a curious hornless robot companion' 290 $meet | Set-Content (Join-Path $assetDir 'agent.svg') -Encoding utf8
$lab = '<text x="40" y="43" font-size="14" letter-spacing="3" class="mint">INSIDE THE LAB / FOUR WAYS TO BUILD</text>'
foreach ($item in @(@(150,110,'SOFTWARE','make it reliable'),@(650,110,'AI','make it learn'),@(150,300,'GAMES','make it alive'),@(650,300,'MATH','understand why'))) {
 $x,$y,$name,$caption = $item
 $lab += "<path class='flow' d='M500 225L$($x+100) $y' fill='none' stroke='#3dffa0' opacity='.5'/><rect x='$x' y='$($y-28)' width='200' height='74' rx='14' fill='#102219' stroke='#365747'/><text x='$($x+100)' y='$y' text-anchor='middle' font-size='20'>$name</text><text x='$($x+100)' y='$($y+25)' text-anchor='middle' font-size='13' class='muted'>$caption</text>"
}
$lab += '<rect x="340" y="194" width="320" height="58" rx="29" fill="#102219" stroke="#3dffa0"/><text x="500" y="230" text-anchor="middle" font-size="22">THINKER × MINDOO</text>'
Frame 'Software, AI, games and mathematics connected through THINKER and MINDOO' 395 $lab | Set-Content (Join-Path $assetDir 'agents.svg') -Encoding utf8
Write-Output 'Built banner.svg, agent.svg and agents.svg'
