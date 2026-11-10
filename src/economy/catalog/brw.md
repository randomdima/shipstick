# Brews & Ferments — `brw`

The drinks that relax. Malted grain from `grn` is mashed and boiled with hops from `veg` into wort; must from `frt`,
berries and melons pressed here, rice mash, sugar wash, sweet tea and bread are pitched with `bio`'s yeasts and
cultures and fermented into ale, stout, lager, wine, cider, kombucha, kefir and kvass; wash is run through the pot still
into spirits, which age in casks. Served in a cup (a dirty dish) or capped into bottles, kegs and flasks. Every brew
eases stress, gives a little fun and adds toxin, spirits the most; kombucha and kefir are mild and good for immunity.
An open brew goes stale and sour into vinegars for `ing` and `cln`; spent grain, yeast, lees, hops and stillage go on
to feed and compost; still heads go to `chm` as solvent.

## Devices

| id | device | role | cells |
|---|---|---|---|
| brw.mashtun | BW120 Mash Tun | galley | 2x1 |
| brw.kettle | BW140 Wort Kettle | galley | 2x1 |
| brw.press | BW210 Cider Press | galley | 2x1 |
| brw.fermenter | BW400 Fermenting Vessel | bio | 2x2 |
| brw.culturecrock | BW45 Culture Crock | bio | 1x1 |
| brw.potstill | BW800 Pot Still | galley | 2x2 |
| brw.cask | BW610 Ageing Rack | galley | 2x1 |
| brw.bottler | BW90 Brew Bottler | galley | 1x1 |

## Items

| id | item | use | decays |
|---|---|---|---|
| brw-001 | Ale, Draught | hydration +8, bladder +18, stress -10, fun +3, toxin +5, leaves 1 cln-001 | 72 h → brw-021 |
| brw-002 | Wine, Grape | hydration +4, bladder +10, stress -12, fun +4, toxin +6, leaves 1 cln-001 | 72 h → brw-047 |
| brw-003 | Cider, Apple | hydration +8, bladder +15, stress -10, fun +3, toxin +4, leaves 1 cln-001 | 72 h → brw-048 |
| brw-004 | Kombucha | hydration +12, bladder +12, stress -4, fun +1, immunity +2, toxin +1, leaves 1 cln-001 | 168 h → brw-049 |
| brw-005 | Wine, Rice | hydration +4, bladder +8, stress -12, fun +4, toxin +7, leaves 1 cln-001 | 168 h → brw-050 |
| brw-006 | Spirit, Grain | hydration -2, bladder +3, stress -15, fun +5, toxin +10, leaves 1 cln-001 | — |
| brw-007 | Ale, Bottled | hydration +10, bladder +20, stress -12, fun +3, toxin +6, leaves 1 pak-004 | — |
| brw-008 | Wine, Bottled | hydration +6, bladder +14, stress -15, fun +5, toxin +9, leaves 1 pak-004 | — |
| brw-009 | Cider, Bottled | hydration +10, bladder +18, stress -12, fun +4, toxin +6, leaves 1 pak-004 | — |
| brw-010 | Kombucha, Bottled | hydration +20, bladder +18, stress -5, fun +1, immunity +3, toxin +1, leaves 1 pak-004 | 720 h → brw-049 |
| brw-011 | Spirit, Bottled | hydration -4, bladder +5, stress -20, fun +8, toxin +16, leaves 1 pak-004 | — |
| brw-012 | Kefir, Water | hydration +12, bladder +12, stress -3, immunity +2, toxin +1, leaves 1 cln-001 | 72 h → san-003 |
| brw-013 | Kvass, Bread | hydration +10, bladder +12, satiety +3, stress -5, fun +1, toxin +2, leaves 1 cln-001 | 72 h → san-003 |
| brw-014 | Stout, Dark | hydration +6, bladder +16, satiety +3, stress -12, fun +3, toxin +6, leaves 1 cln-001 | 72 h → brw-021 |
| brw-015 | Beer, Wheat | hydration +8, bladder +18, satiety +1, stress -10, fun +3, toxin +5, leaves 1 cln-001 | 72 h → brw-021 |
| brw-016 | Lager, Rice | hydration +9, bladder +18, stress -9, fun +3, toxin +4, leaves 1 cln-001 | 72 h → brw-021 |
| brw-017 | Beer, Small | hydration +12, bladder +15, stress -5, fun +1, toxin +2, leaves 1 cln-001 | 72 h → brw-021 |
| brw-018 | Beer, Ginger | hydration +10, bladder +15, stress -6, fun +3, toxin +2, leaves 1 cln-001 | 72 h → san-003 |
| brw-019 | Ale, Spiced | hydration +7, bladder +16, stress -12, fun +4, toxin +6, leaves 1 cln-001 | 72 h → brw-021 |
| brw-020 | Ale, Algae | hydration +8, bladder +16, stress -8, fun +5, immunity +1, toxin +5, leaves 1 cln-001 | 72 h → brw-021 |
| brw-021 | Beer, Stale | hydration +6, bladder +15, stress -4, toxin +5, leaves 1 cln-001 | 168 h → brw-046 |
| brw-022 | Wine, Berry | hydration +4, bladder +10, stress -12, fun +4, toxin +6, leaves 1 cln-001 | 72 h → brw-047 |
| brw-023 | Wine, Melon | hydration +5, bladder +11, stress -11, fun +4, toxin +6, leaves 1 cln-001 | 72 h → brw-047 |
| brw-024 | Wine, Citrus | hydration +4, bladder +10, stress -11, fun +4, immunity +1, toxin +6, leaves 1 cln-001 | 72 h → brw-047 |
| brw-025 | Wine, Sparkling | hydration +4, bladder +12, stress -14, fun +6, toxin +6, leaves 1 cln-001 | 24 h → brw-002 |
| brw-026 | Wine, Mulled | hydration +4, bladder +10, stress -15, fun +4, toxin +6, leaves 1 cln-001 | 12 h → brw-002 |
| brw-027 | Wine, Rice, Sweet | hydration +4, bladder +8, satiety +2, stress -12, fun +5, toxin +7, leaves 1 cln-001 | 168 h → brw-050 |
| brw-028 | Wine, Fortified | hydration +2, bladder +8, stress -15, fun +4, toxin +10, leaves 1 cln-001 | — |
| brw-029 | Spritzer, Wine | hydration +10, bladder +14, stress -8, fun +4, toxin +3, leaves 1 cln-001 | 24 h → san-003 |
| brw-030 | Cider, Berry | hydration +8, bladder +15, stress -10, fun +4, toxin +4, leaves 1 cln-001 | 72 h → brw-048 |
| brw-031 | Kombucha, Hard | hydration +10, bladder +12, stress -10, fun +3, immunity +1, toxin +5, leaves 1 cln-001 | 168 h → brw-049 |
| brw-032 | Kombucha, Ginger | hydration +12, bladder +12, stress -5, fun +2, immunity +2, toxin +1, leaves 1 cln-001 | 168 h → brw-049 |
| brw-033 | Kombucha, Berry | hydration +12, bladder +12, stress -4, fun +2, immunity +3, toxin +1, leaves 1 cln-001 | 168 h → brw-049 |
| brw-034 | Soda, Fruit, Fermented | hydration +10, bladder +14, stress -4, fun +3, toxin +1, leaves 1 cln-001 | 72 h → san-003 |
| brw-035 | Amazake, Rice | hydration +8, bladder +8, satiety +5, stress -4, fun +1, toxin +1, leaves 1 cln-001 | 48 h → san-003 |
| brw-036 | Spirit, Rice | hydration -2, bladder +3, stress -15, fun +5, toxin +10, leaves 1 cln-001 | — |
| brw-037 | Spirit, Potato | hydration -2, bladder +3, stress -15, fun +4, toxin +11, leaves 1 cln-001 | — |
| brw-038 | Brandy, Fruit | hydration -2, bladder +3, stress -16, fun +6, toxin +10, leaves 1 cln-001 | — |
| brw-039 | Liqueur, Berry | hydration -1, bladder +3, satiety +1, stress -12, fun +6, toxin +7, leaves 1 cln-001 | — |
| brw-040 | Bitters, Herbal | bladder +2, stress -10, pain -2, toxin +6, leaves 1 cln-001 | — |
| brw-041 | Spirit, Cask Aged | hydration -2, bladder +3, stress -18, fun +7, toxin +10, leaves 1 cln-001 | — |
| brw-042 | Hooch, Ship | hydration -3, bladder +3, stress -15, fun +4, toxin +16, leaves 1 cln-001 | — |
| brw-043 | Toddy, Hot | hydration +6, bladder +8, stress -16, fun +4, pain -2, toxin +6, leaves 1 cln-001 | 12 h → san-003 |
| brw-044 | Highball, Spirit | hydration +8, bladder +12, stress -12, fun +6, toxin +6, leaves 1 cln-001 | 24 h → san-003 |
| brw-045 | Shandy | hydration +12, bladder +16, stress -6, fun +3, toxin +2, leaves 1 cln-001 | 24 h → san-003 |
| brw-046 | Vinegar, Malt | — | — |
| brw-047 | Vinegar, Wine | — | — |
| brw-048 | Vinegar, Cider | — | — |
| brw-049 | Vinegar, Kombucha | — | — |
| brw-050 | Wine, Rice, Sour | — | — |
| brw-051 | Malt, Roasted | — | — |
| brw-052 | Malt, Wheat | — | — |
| brw-053 | Mash, Grain | — | 24 h → san-003 |
| brw-054 | Wort, Sweet | — | 24 h → san-003 |
| brw-055 | Wort, Hopped | — | 24 h → san-003 |
| brw-056 | Mash, Rice | — | 24 h → san-003 |
| brw-057 | Mash, Potato, Brewing | — | 24 h → san-003 |
| brw-058 | Must, Berry | — | 48 h → san-003 |
| brw-059 | Wash, Sugar | — | 72 h → san-003 |
| brw-060 | Base, Sweet Tea | — | 48 h → san-003 |
| brw-061 | Mash, Kvass Bread | — | 48 h → san-003 |
| brw-062 | Beer, Green | — | 72 h → brw-021 |
| brw-063 | Wine, Young | — | — |
| brw-064 | Cider, Young | — | — |
| brw-065 | Wash, Fermented | — | 72 h → san-003 |
| brw-066 | Distillate, Low Wines | — | — |
| brw-067 | Heads, Still | — | — |
| brw-068 | Tails, Still | — | — |
| brw-069 | Grain, Spent | — | 72 h → san-003 |
| brw-070 | Slurry, Yeast, Spent | — | 72 h → san-003 |
| brw-071 | Lees, Wine | — | 72 h → san-003 |
| brw-072 | Stillage | — | 48 h → san-003 |
| brw-073 | Hops, Spent | — | 72 h → san-002 |
| brw-074 | Keg, Brew, Empty | — | — |
| brw-075 | Keg, Ale | — | — |
| brw-076 | Beer, Ginger, Bottled | hydration +15, bladder +18, stress -8, fun +3, toxin +2, leaves 1 pak-004 | — |
| brw-077 | Kvass, Bottled | hydration +15, bladder +16, satiety +3, stress -6, fun +1, toxin +2, leaves 1 pak-004 | 720 h → san-003 |
| brw-078 | Stout, Bottled | hydration +8, bladder +18, satiety +3, stress -14, fun +3, toxin +7, leaves 1 pak-004 | — |
| brw-079 | Wine, Rice, Bottled | hydration +6, bladder +12, stress -15, fun +5, toxin +9, leaves 1 pak-004 | — |
| brw-080 | Liqueur, Berry, Bottled | hydration -2, bladder +5, satiety +2, stress -18, fun +8, toxin +12, leaves 1 pak-004 | — |
| brw-081 | Flask, Hip, Filled | hydration -1, bladder +2, stress -10, fun +4, toxin +8, leaves 1 brw-082 | — |
| brw-082 | Flask, Hip, Empty | — | — |
| brw-083 | False Bottom, Mash Tun | fits brw.mashtun | — |
| brw-084 | Element, Wort Kettle | fits brw.kettle | — |
| brw-085 | Bag, Cider Press | fits brw.press | — |
| brw-086 | Airlock, Fermenting Vessel | fits brw.fermenter | — |
| brw-087 | Gasket, Lid, Fermenting Vessel | fits brw.fermenter | — |
| brw-088 | Cover, Cloth, Culture Crock | fits brw.culturecrock | — |
| brw-089 | Coil, Copper, Pot Still | fits brw.potstill | — |
| brw-090 | Helmet, Pot Still | fits brw.potstill | — |
| brw-091 | Staves, Ageing Rack | fits brw.cask | — |
| brw-092 | Capping Bell, Brew Bottler | fits brw.bottler | — |
| brw-093 | Kit, Mash Tun | installs brw.mashtun | — |
| brw-094 | Kit, Wort Kettle | installs brw.kettle | — |
| brw-095 | Kit, Cider Press | installs brw.press | — |
| brw-096 | Kit, Fermenting Vessel | installs brw.fermenter | — |
| brw-097 | Kit, Culture Crock | installs brw.culturecrock | — |
| brw-098 | Kit, Pot Still | installs brw.potstill | — |
| brw-099 | Kit, Ageing Rack | installs brw.cask | — |
| brw-100 | Kit, Brew Bottler | installs brw.bottler | — |

## Ways

| way | by | min | takes | makes | gives |
|---|---|---|---|---|---|
| roast malt | brw.kettle | 60 | 2 grn-058, 1 pwr-001 | 2 brw-051 | — |
| malt wheat | brw.mashtun | 240 | 3 grn-001, 2 wat-001, 1 pwr-001 | 3 brw-052 | — |
| mash barley malt | brw.mashtun | 90 | 3 grn-058, 3 wat-009, 1 pwr-001 | 2 brw-053 | — |
| mash wheat malt | brw.mashtun | 90 | 2 brw-052, 1 grn-058, 3 wat-009, 1 pwr-001 | 2 brw-053 | — |
| lauter the mash | brw.mashtun | 30 | 2 brw-053, 2 wat-001 | 2 brw-054, 2 brw-069 | — |
| steam and mash rice | brw.mashtun | 60 | 3 grn-003, 2 wat-009, 1 pwr-001 | 3 brw-056 | — |
| mash potatoes for brewing | brw.mashtun | 90 | 3 grn-004, 2 wat-009, 1 pwr-001 | 3 brw-057 | — |
| dissolve a sugar wash | brw.mashtun | 30 | 2 ing-051, 3 wat-009 | 3 brw-059 | — |
| soak stale bread | brw.mashtun | 120 | 2 mel-080, 3 wat-001 | 2 brw-061 | — |
| boil wort with dried hops | brw.kettle | 60 | 2 brw-054, 1 veg-076, 1 pwr-001 | 2 brw-055, 1 brw-073 | — |
| boil wort with fresh hops | brw.kettle | 60 | 2 brw-054, 2 veg-035, 1 pwr-001 | 2 brw-055, 1 brw-073 | — |
| brew sweet tea base | brw.kettle | 20 | 1 bev-019, 1 ing-003, 3 wat-001, 1 pwr-001 | 3 brw-060, 1 san-002 | — |
| press berries for must | brw.press | 30 | 4 frt-063, 1 pwr-001 | 3 brw-058, 1 frt-009 | — |
| ferment ale | brw.fermenter | 720 | 3 brw-055, 1 bio-050 | 3 brw-062, 1 brw-070, 1 gas-002 | — |
| ferment stout | brw.fermenter | 720 | 3 brw-055, 1 brw-051, 1 bio-050, 3 cln-002 | 3 brw-014, 1 brw-070, 1 gas-002 | — |
| ferment wheat beer | brw.fermenter | 720 | 3 brw-055, 1 brw-052, 1 bio-050, 3 cln-002 | 3 brw-015, 1 brw-070, 1 gas-002 | — |
| ferment rice lager | brw.fermenter | 960 | 2 brw-055, 1 brw-056, 1 bio-050, 3 cln-002 | 3 brw-016, 1 brw-070, 1 gas-002 | — |
| ferment small beer | brw.fermenter | 480 | 1 brw-055, 3 wat-001, 1 brw-070, 3 cln-002 | 3 brw-017, 1 gas-002 | — |
| ferment spiced ale | brw.fermenter | 720 | 3 brw-055, 1 ing-004, 1 bio-050, 3 cln-002 | 3 brw-019, 1 brw-070, 1 gas-002 | — |
| ferment algae ale | brw.fermenter | 720 | 3 brw-055, 1 prt-031, 1 bio-050, 3 cln-002 | 3 brw-020, 1 brw-070, 1 gas-002 | — |
| condition ale into a keg | brw.cask | 1440 | 4 brw-062, 1 brw-074 | 1 brw-075 | — |
| tap the ale keg | crew | 5 | 1 brw-075, 4 cln-002 | 4 brw-001, 1 brw-074 | — |
| bottle ale | brw.bottler | 30 | 2 brw-062, 2 pak-003, 1 ing-003 | 2 brw-007, 1 gas-002 | — |
| bottle stout | brw.bottler | 1440 | 3 brw-055, 1 brw-051, 1 bio-050, 3 pak-003 | 3 brw-078, 1 brw-070, 1 gas-002 | — |
| ferment grape must | brw.fermenter | 1440 | 4 frt-048, 1 bio-051 | 3 brw-063, 1 brw-071, 1 gas-002 | — |
| age and draw wine | brw.cask | 1440 | 3 brw-063, 3 cln-002 | 3 brw-002 | — |
| bottle young wine | brw.bottler | 60 | 2 brw-063, 2 pak-003 | 2 brw-008 | — |
| ferment berry wine | brw.fermenter | 1440 | 3 brw-058, 1 bio-051, 3 cln-002 | 3 brw-022, 1 brw-071, 1 gas-002 | — |
| ferment melon wine | brw.fermenter | 1440 | 2 frt-008, 1 ing-003, 1 bio-051, 3 cln-002 | 3 brw-023, 1 brw-071, 1 gas-002 | — |
| ferment citrus wine | brw.fermenter | 1440 | 3 frt-004, 1 ing-003, 1 bio-051, 3 cln-002 | 3 brw-024, 1 brw-071, 1 gas-002 | — |
| sparkle young wine | brw.bottler | 20 | 2 brw-063, 1 gas-043, 2 cln-002, 1 pwr-001 | 2 brw-025 | — |
| mull wine | brw.kettle | 20 | 2 brw-002, 1 ing-004, 1 pwr-001 | 2 brw-026 | — |
| fortify wine | brw.cask | 720 | 3 brw-002, 1 brw-006 | 3 brw-028, 1 cln-001 | — |
| mix a wine spritzer | crew | 3 | 1 brw-002, 1 wat-046, 1 cln-002 | 2 brw-029 | — |
| ferment rice wine | brw.fermenter | 1440 | 3 brw-056, 1 bio-059, 1 bio-051, 3 cln-002 | 3 brw-005, 1 brw-071, 1 gas-002 | — |
| ferment sweet rice wine | brw.fermenter | 1440 | 3 brw-056, 1 bio-059, 1 ing-003, 3 cln-002 | 3 brw-027, 1 brw-071, 1 gas-002 | — |
| bottle rice wine | brw.bottler | 1440 | 3 brw-056, 1 bio-059, 3 pak-003 | 3 brw-079, 1 gas-002 | — |
| ferment apple must | brw.fermenter | 1440 | 4 frt-049, 1 bio-051 | 3 brw-064, 1 brw-071, 1 gas-002 | — |
| draw cider | brw.cask | 240 | 3 brw-064, 3 cln-002 | 3 brw-003 | — |
| bottle cider | brw.bottler | 30 | 2 brw-064, 2 pak-003 | 2 brw-009 | — |
| ferment berry cider | brw.fermenter | 1440 | 2 frt-049, 1 brw-058, 1 bio-051, 3 cln-002 | 3 brw-030, 1 brw-071, 1 gas-002 | — |
| ferment kombucha | brw.culturecrock | 1440 | 3 brw-060, 1 bio-057, 3 cln-002 | 3 brw-004, 1 gas-002 | — |
| flavour ginger kombucha | brw.culturecrock | 480 | 2 brw-004, 1 bev-040 | 2 brw-032 | — |
| flavour berry kombucha | brw.culturecrock | 480 | 2 brw-004, 1 frt-063 | 2 brw-033 | — |
| ferment hard kombucha | brw.fermenter | 720 | 2 brw-004, 1 ing-003, 1 bio-051 | 2 brw-031, 1 gas-002 | — |
| bottle kombucha | brw.bottler | 1440 | 3 brw-060, 1 bio-057, 3 pak-003 | 3 brw-010, 1 gas-002 | — |
| ferment water kefir | brw.culturecrock | 1440 | 1 bio-056, 1 ing-003, 3 wat-001, 3 cln-002 | 3 brw-012 | — |
| ferment kvass | brw.culturecrock | 1440 | 2 brw-061, 1 bio-009, 1 ing-003, 3 cln-002 | 3 brw-013, 1 gas-002 | — |
| bottle kvass | brw.bottler | 1440 | 2 brw-061, 1 bio-009, 2 pak-003 | 2 brw-077, 1 gas-002 | — |
| ferment ginger beer | brw.culturecrock | 480 | 1 bev-040, 1 ing-003, 3 wat-001, 1 bio-009, 3 cln-002 | 3 brw-018, 1 gas-002 | — |
| bottle ginger beer | brw.bottler | 720 | 1 bev-040, 1 ing-003, 3 wat-001, 1 bio-009, 3 pak-003 | 3 brw-076, 1 gas-002 | — |
| ferment a fruit soda | brw.culturecrock | 720 | 1 bev-039, 1 bio-056, 3 wat-001, 3 cln-002 | 3 brw-034, 1 gas-002 | — |
| culture rice amazake | brw.culturecrock | 720 | 2 brw-056, 1 bio-059, 2 cln-002 | 2 brw-035 | — |
| ferment a sugar wash | brw.fermenter | 1440 | 3 brw-059, 1 bio-049 | 3 brw-065, 1 gas-002 | — |
| ferment a grain wash | brw.fermenter | 1440 | 3 brw-054, 1 bio-049 | 3 brw-065, 1 gas-002 | — |
| strip the wash | brw.potstill | 120 | 3 brw-065, 2 pwr-001 | 2 brw-066, 2 brw-072 | — |
| run grain spirit | brw.potstill | 120 | 2 brw-066, 2 cln-002, 1 pwr-001 | 2 brw-006, 1 brw-067, 1 brw-068 | — |
| run spirit into bottles | brw.potstill | 120 | 2 brw-066, 2 pak-003, 1 pwr-001 | 2 brw-011, 1 brw-067, 1 brw-068 | — |
| rerun the tails | brw.potstill | 60 | 3 brw-068, 1 pwr-001 | 1 brw-066 | — |
| distil rice spirit | brw.potstill | 180 | 3 brw-056, 1 bio-059, 2 cln-002, 2 pwr-001 | 2 brw-036, 2 brw-072, 1 brw-067 | — |
| distil potato spirit | brw.potstill | 180 | 3 brw-057, 1 bio-049, 2 cln-002, 2 pwr-001 | 2 brw-037, 2 brw-072, 1 brw-067 | — |
| distil fruit brandy | brw.potstill | 180 | 3 brw-063, 1 cln-002, 2 pwr-001 | 1 brw-038, 2 brw-072 | — |
| run a bench hooch | any.bench | 240 | 3 brw-065, 2 cln-002, 2 pwr-001 | 2 brw-042, 1 brw-072 | — |
| steep berry liqueur | brw.cask | 1440 | 2 brw-006, 1 frt-063, 1 ing-003 | 2 brw-039 | — |
| bottle berry liqueur | brw.cask | 1440 | 2 brw-066, 1 frt-063, 1 ing-003, 2 pak-003 | 2 brw-080 | — |
| steep herbal bitters | brw.cask | 1440 | 2 brw-006, 1 veg-071 | 2 brw-040 | — |
| cask age spirit | brw.cask | 2880 | 3 brw-006 | 3 brw-041 | — |
| mix a hot toddy | brw.kettle | 10 | 1 brw-006, 1 bev-040, 1 wat-006, 1 pwr-001 | 1 brw-043 | — |
| mix a spirit highball | crew | 3 | 1 brw-006, 1 wat-046, 1 wat-013, 1 cln-002 | 2 brw-044 | — |
| mix a shandy | crew | 3 | 1 brw-001, 1 bev-052 | 2 brw-045 | — |
| fill a hip flask | crew | 5 | 1 brw-082, 1 brw-011 | 1 brw-081, 1 pak-004 | — |
| sour rice wine into vinegar | brw.culturecrock | 720 | 3 brw-050, 1 bio-058 | 3 ing-077 | — |
| wipe down with malt vinegar | crew | 15 | 1 brw-046 | — | cabin.clean +4 |
| wipe down with wine vinegar | crew | 15 | 1 brw-047 | — | cabin.clean +4 |
| wipe down with cider vinegar | crew | 15 | 1 brw-048 | — | cabin.clean +4 |
| wipe down with kombucha vinegar | crew | 15 | 1 brw-049 | — | cabin.clean +3 |
| wipe down with still heads | crew | 15 | 1 brw-067 | — | cabin.clean +5, toxin +1 |
| make a brew keg | any.bench | 60 | 1 met-034, 1 pak-046 | 1 brw-074 | — |
| make a hip flask | any.bench | 30 | 1 met-034 | 1 brw-082 | — |
| make a mash tun false bottom | any.bench | 45 | 1 met-034 | 1 brw-083 | — |
| make a wort kettle element | any.bench | 30 | 1 met-047, 1 cer-035 | 1 brw-084 | — |
| sew a cider press bag | any.bench | 20 | 1 fib-008 | 1 brw-085 | — |
| make fermenter airlocks | any.bench | 20 | 1 cer-019, 1 pol-048 | 2 brw-086 | — |
| cut fermenter lid gaskets | any.bench | 15 | 1 pol-052 | 2 brw-087 | — |
| hem culture crock covers | any.bench | 15 | 1 fib-064 | 2 brw-088 | — |
| wind a pot still copper coil | any.bench | 60 | 2 met-053 | 1 brw-089 | — |
| beat a pot still helmet | any.bench | 90 | 1 met-037 | 1 brw-090 | — |
| cut cask rack staves | any.bench | 45 | 2 fur-002 | 1 brw-091 | — |
| make a bottler capping bell | any.bench | 45 | 1 met-049, 1 mec-005 | 1 brw-092 | — |
| pack a mash tun kit | any.bench | 120 | 1 fur-001, 1 brw-083, 1 met-034 | 1 brw-093 | — |
| pack a wort kettle kit | any.bench | 120 | 1 fur-001, 1 brw-084, 1 met-034 | 1 brw-094 | — |
| pack a cider press kit | any.bench | 120 | 1 fur-001, 1 brw-085, 1 mec-030 | 1 brw-095 | — |
| pack a fermenting vessel kit | any.bench | 120 | 1 fur-001, 1 brw-086, 1 brw-087, 1 met-034 | 1 brw-096 | — |
| pack a culture crock kit | any.bench | 60 | 1 fur-001, 1 brw-088, 1 cer-031 | 1 brw-097 | — |
| pack a pot still kit | any.bench | 120 | 1 fur-001, 1 brw-089, 1 brw-090 | 1 brw-098 | — |
| pack an ageing rack kit | any.bench | 90 | 1 fur-001, 1 brw-091 | 1 brw-099 | — |
| pack a brew bottler kit | any.bench | 90 | 1 fur-001, 1 brw-092, 1 mec-043 | 1 brw-100 | — |

## Codex

| id | about | flavour |
|---|---|---|
| brw.mashtun | Malts wheat and mashes grain, rice, potatoes, sugar and stale bread for brewing, and lauters mash into wort. | Mash temperature per Brewing Proc 120. Stirring paddle is station inventory. Ref 1204/M. |
| brw.kettle | Boils wort with hops, roasts malt, brews sweet tea base, mulls wine and mixes hot toddies. | BOIL-OVER HAZARD. DO NOT LEAVE DURING HOP ADDITION. |
| brw.press | Presses berries into must for wine and cider, leaving pomace. | Screw thread regreased, rev 3. Press bag patched twice. Still holds. |
| brw.fermenter | Ferments wort, must, mash and wash with yeast into beers, wines and washes, venting carbon dioxide. | Fermentation gas is vented to cabin air. Scrubber load is the station's concern. Notice 400/F. |
| brw.culturecrock | Grows kombucha, kefir, kvass, ginger beer, fermented soda and amazake, and sours rice wine to vinegar. | LIVE CULTURE. DO NOT DISTURB. DO NOT FEED OUTSIDE SCHEDULE. |
| brw.potstill | Strips wash into low wines and runs them into spirit, leaving heads, tails and stillage. | Registered as solvent recovery equipment. Its other output is not recorded. Ref 8000/S. |
| brw.cask | Conditions ale into kegs, ages and fortifies wine, ages spirit, draws cider, and steeps liqueurs and bitters. | Ageing time is unproductive time. It is billed to the rack, not the operator. Ref 6100/A. |
| brw.bottler | Bottles beers, wines, kombucha, kvass and ginger beer for keeping, and sparkles young wine. | Capping bell aligned, rev 2. Two bottles lost in test. Written off. |
| brw-001 | Ale tapped from a conditioned keg and served in a cup; relaxing, mildly toxic, and goes stale if left. | Consumption on shift is not prohibited. Errors on shift are not excused. Notice 0011/A. |
| brw-002 | Grape wine drawn from the ageing rack and served in a cup; relaxing, and sours to vinegar if left. | Vintage: this year. It is always this year. |
| brw-003 | Apple cider drawn from young cider and served in a cup; relaxing, and sours to vinegar if left. | APPLE CIDER. FERMENTED. NOT JUICE. NOT FOR MEDKITS. |
| brw-004 | Sweet tea fermented by a kombucha culture; mildly relaxing, supports immunity, and sours to vinegar in time. | The culture is Company property. Its offspring are Company property. Ref 0404/K. |
| brw-005 | Rice mash fermented with koji and yeast; strongly relaxing, and sours in time. | Small cups only. Large cups are not issued for a reason. |
| brw-006 | Clear spirit run from low wines; strongly relaxing and toxic, and the base of liqueurs, bitters and mixed drinks. | CLEAR LIQUID. NOT WATER. NOT FOR COOLANT TOP-UP. |
| brw-007 | Green beer bottled with sugar to condition; keeps until opened and leaves an empty bottle. | Secondary fermentation may pressurise the bottle. Shrapnel injuries are self-inflicted. Proc 77. |
| brw-008 | Young wine bottled for keeping; leaves an empty bottle. | Kept for an occasion. Occasions are not scheduled here. |
| brw-009 | Young cider bottled for keeping; leaves an empty bottle. | Batch sampled, label applied, rev 1. Sampler's notes withheld. |
| brw-010 | Kombucha fermented in the bottle; supports immunity, and sours to vinegar eventually. | VENT CAP WEEKLY. LIVE FERMENT UNDER PRESSURE. |
| brw-011 | Spirit run straight into bottles; the strongest and most toxic drink aboard, used to fill hip flasks. | Unofficial door slot currency. The Company neither recognises nor taxes it. Yet. |
| brw-012 | Sweetened water fermented with kefir grains; mild, and supports immunity. | Grains that are not grain. Ferment that barely is. Approved anyway. |
| brw-013 | Stale bread fermented into a mild, slightly filling drink. | Bread waste reclassified as beverage stock. Waste figures improved. Ref 1330/B. |
| brw-014 | Stout fermented with roasted malt; filling and relaxing, and goes stale if left. | Dark as the outside. Warmer, marginally. |
| brw-015 | Beer fermented with wheat malt; cloudy, relaxing and slightly filling. | CLOUDY BY SPECIFICATION. NOT A FAULT. DO NOT REPORT. |
| brw-016 | A light lager fermented from hopped wort and rice mash; relaxing. | Crisp enough to cut the recycled air. Not enough to improve it. |
| brw-017 | Weak beer of thinned wort and spent yeast; hydrating and mild. | Low strength beverage. Approved for consumption during operation, Proc 17B. |
| brw-018 | Ginger syrup fermented with yeast; fizzy, mild and recreational. | Mildly alcoholic. Classified as a soft drink for inventory convenience. Ref 1880/G. |
| brw-019 | Ale fermented with spice mix; relaxing, and goes stale if left. | Brewed for the turning of the fiscal year. The only holiday on the schedule. |
| brw-020 | Ale fermented with spirulina; green, recreational, with a touch of immune support. | It is green. It is ale. No further questions will be taken. |
| brw-021 | Beer gone flat; still drinkable, and sours into malt vinegar. | Nobody finishes it. Somebody always pours it. |
| brw-022 | Wine fermented from berry must; relaxing, and sours to vinegar if left. | Purple staining of teeth is cosmetic and not a medical claim. Form 22P refused. |
| brw-023 | Wine fermented from melons and sugar; relaxing, and sours to vinegar if left. | Sweet start, sour finish. Like the contract. |
| brw-024 | Wine fermented from mandarins and sugar; relaxing, with a touch of immune support. | Grown under lamps, fermented in the dark, logged in triplicate. |
| brw-025 | Young wine carbonated from a gas cartridge; goes flat into plain grape wine quickly. | CARBONATED. POINT AWAY FROM VIEWPORTS AND PERSONNEL. |
| brw-026 | Grape wine warmed with spice; cools back into plain grape wine. | Warms the hands. Cabin heating budget unchanged. Notice 26/H. |
| brw-027 | Rice wine fermented with extra sugar; sweet, relaxing and slightly filling. | Dessert, technically. Not counted against the ration, technically. |
| brw-028 | Grape wine strengthened with spirit in the cask; it does not spoil. | Keeps indefinitely. Rarely given the opportunity. |
| brw-029 | Grape wine stretched with sparkling water; light and recreational. | Wine stock extended by dilution per Economy Directive 29. Morale effect unmeasured. |
| brw-030 | Cider fermented from apple and berry must; relaxing, and sours to vinegar if left. | Pink, fizzy, gone. Log the bottle, not the evening. |
| brw-031 | Kombucha fermented again with wine yeast and sugar into a stronger, more toxic drink. | Second ferment exceeds the soft drink threshold. Reclassified. Ref 3101/K. |
| brw-032 | Kombucha flavoured with ginger syrup; supports immunity. | GINGER FLAVOURED. CULTURE ACTIVE. KEEP COOL. |
| brw-033 | Kombucha flavoured with berries; the kombucha that best supports immunity. | Tangy, pink and suspiciously healthy. Medbay asks no questions. |
| brw-034 | Berry cordial fermented with kefir grains into a fizzy, mild drink. | Self-carbonating. Uses no gas cartridge. Savings credited to the Company. |
| brw-035 | Rice mash cultured with koji into a sweet, filling drink. | Sweet without sugar. The koji does the work and receives no wage. |
| brw-036 | Spirit distilled from koji rice mash; strongly relaxing and toxic. | Distillate tested, rev 4. Proof within tolerance. Tester stood down for the shift. |
| brw-037 | Spirit distilled from potato mash; strongly relaxing and toxic. | Potato allocation diverted from food stock. Diversion noted. Ref 3700/P. |
| brw-038 | Brandy distilled from young wine; strongly relaxing and toxic. | A whole crop of fruit in one cup. The crop was not consulted. |
| brw-039 | Grain spirit steeped with berries and sugar; sweet, relaxing and toxic. | Sweet as an apology, strong as a grudge. |
| brw-040 | Spirit steeped with dried herbs; bitter, easing stress and pain. | Not a licensed medicine. Do not list on Form 40M as treatment. |
| brw-041 | Grain spirit aged long in the cask; the most relaxing spirit aboard. | AGED IN RACK 4. OLDER THAN SOME CONTRACTS. |
| brw-042 | Rough spirit run from wash on a workbench; strong and very toxic. | Unauthorised. Unlabelled. Confiscated, then misplaced. |
| brw-043 | Spirit with ginger syrup and hot water; calming, and eases pain. | Medicine, for a given value of medicine. |
| brw-044 | Grain spirit served over ice with sparkling water; relaxing and recreational. | Ice and sparkling water drawn from cabin stock. Draws logged. Ref 4400/H. |
| brw-045 | Ale mixed with lemonade; light, recreational and mild. | Half ale, half lemonade, entirely a compromise. |
| brw-046 | Stale beer soured to vinegar, for wiping down the cabin. | MALT VINEGAR. CLEANING USE. DO NOT DRINK. |
| brw-047 | Wine soured to vinegar, for wiping down the cabin. | Every failed vintage is a successful cleaner. Waste rate restated accordingly. |
| brw-048 | Cider soured to vinegar, for wiping down the cabin. | Wipe the bench. Leave the mother in the jar. |
| brw-049 | Kombucha soured to vinegar; a mild cleaner for the cabin. | Weaker than malt vinegar. Approved for light soiling only, Proc 49. |
| brw-050 | Rice wine gone sour, cultured into rice vinegar. | Turned, not ruined. Reclassified, not written off. |
| brw-051 | Malted barley roasted dark, for stout. | Burnt on purpose this time. Log entry amended. |
| brw-052 | Sprouted wheat for wheat beer and the mash. | GERMINATED GRAIN. NOT SEED STOCK. DO NOT PLANT. |
| brw-053 | Malt steeped in hot water, lautered into sweet wort and spent grain. | Porridge with prospects. Not for breakfast. |
| brw-054 | Sugary liquid run off the mash; boiled with hops, or fermented into wash. | Tasting of wort is not a quality step. Sticky panels are cleaned by the taster. |
| brw-055 | Wort boiled with hops, ready to ferment into beer. | Bitter now. Beer later. Probably. |
| brw-056 | Steamed rice mash for rice wine, lager, amazake and rice spirit. | Rice diverted from food stock to brewing under Allocation 56. Diversion approved. |
| brw-057 | Potatoes mashed for distilling into spirit. | NOT FOR CONSUMPTION AS FOOD. DISTILLATION STOCK. |
| brw-058 | Pressed berries for berry wine and berry cider. | Purple everywhere. On everything. Including the log. |
| brw-059 | Molasses dissolved in water, fermented into wash for distilling. | Molasses issued for baking. Usage audit pending. Ref 5900/W. |
| brw-060 | Sweetened black tea for growing kombucha. | Feed the culture on schedule. An unfed culture is a written report. |
| brw-061 | Stale bread soaked for fermenting into kvass. | No crust left behind. Proc 61 does not allow it. |
| brw-062 | Young beer straight off the fermenter, conditioned into a keg or bottled; goes stale if left. | GREEN BEER. UNCONDITIONED. NOT FOR ISSUE. |
| brw-063 | Freshly fermented wine, to be aged, bottled, sparkled or distilled. | Rough now. Given time. Time is the one thing in surplus. |
| brw-064 | Freshly fermented cider, to be drawn or bottled. | Clarity test failed, rev 1. Passed as cloudy cider, rev 2. |
| brw-065 | Fermented sugar or grain wash, stripped in the pot still. | Smells foul. Distils clean. Containment lid stays shut. |
| brw-066 | The first run off the still, run again into spirit or liqueur. | INTERMEDIATE PRODUCT. NOT FOR ISSUE. RETURN TO STILL. |
| brw-067 | The harsh first cut off the still; never drunk, but a strong cleaner. | Toxic. Approved as a cleaning solvent under Proc 67. Ventilate after use. |
| brw-068 | The weak last cut off the still, rerun into low wines. | Round again. Nothing leaves the still unless it is spirit or waste. |
| brw-069 | Grain left after lautering, for compost and feed pellets. | Too good to waste, too chewy to eat. Sent to feed. |
| brw-070 | Used yeast from the fermenter, for small beer, washing or repitching. | Repitch count, rev 7. Strain drift suspected. Not investigated. |
| brw-071 | Sediment left by wine and cider; its yeast can be recovered. | Dregs are recoverable stock. Disposal without recovery is a loss. Ref 7100/L. |
| brw-072 | Spent liquid left in the still, sent to compost. | HOT RESIDUE. COOL BEFORE TRANSFER TO COMPOST. |
| brw-073 | Boiled hops, sent to compost; turns to food scraps if left. | Bitter to the end. Then compost. |
| brw-074 | An empty steel keg for conditioning ale. | Returnable container. Dents are assessed on return. Form 74K. |
| brw-075 | A keg of conditioned ale, tapped into cups; returns the empty keg. | Tap gently. Sound carries further than voice traffic is allowed to. |
| brw-076 | Ginger beer fermented in the bottle; keeps until opened and leaves an empty bottle. | STORE UPRIGHT. OPEN AWAY FROM FACE. |
| brw-077 | Kvass fermented in the bottle; slightly filling, and spoils in time. | Bread, bottled. Inventory has stopped asking. |
| brw-078 | Stout fermented in the bottle; it does not spoil and leaves an empty bottle. | Heavy for its size. Passes through the door slot with effort. |
| brw-079 | Rice wine fermented in the bottle; it does not spoil and leaves an empty bottle. | Bottle conditioned, sealed and stamped, rev 3. Stamp ink ran. |
| brw-080 | Berry liqueur steeped and bottled; very strong and toxic. | Gifts between stations are not recognised as transactions. Notice 80/G. |
| brw-081 | A hip flask filled with spirit; leaves the empty flask. | Personal containers of spirit are permitted off shift. Off shift is not defined. |
| brw-082 | An empty steel flask, filled from a bottle of spirit. | Light. Suspiciously light. |
| brw-083 | A replacement false bottom fitted to the mash tun. | Perforations cleared, rev 5. Grain stays in, wort runs out. |
| brw-084 | A replacement heating element fitted to the wort kettle. | Boil-over shortens element life. Replacements are deducted. Ref 8400/E. |
| brw-085 | A replacement canvas bag fitted to the cider press. | CANVAS. RINSE AFTER USE. REPLACE WHEN TORN. |
| brw-086 | A replacement airlock fitted to the fermenting vessel. | Blip. Blip. Blip. Nominal. |
| brw-087 | A replacement lid gasket fitted to the fermenting vessel. | Seal test passed, rev 2. Odour test failed. Odour accepted. |
| brw-088 | A replacement muslin cover fitted to the culture crock. | Lets the culture breathe. Keeps the dust out. Most of it. |
| brw-089 | A replacement copper coil fitted to the pot still. | Copper is a controlled material. Coil weight is checked at each inspection. Proc 89. |
| brw-090 | A replacement copper helmet fitted to the pot still. | Polishing is not a maintenance task. It is done anyway. |
| brw-091 | Replacement staves fitted to the ageing rack. | LAMINATE. NOT OAK. FLAVOUR CLAIMS VOID. |
| brw-092 | A replacement capping bell fitted to the brew bottler. | Ding. Sealed. Next. |
| brw-093 | A packed mash tun, ready to install. | Brewing equipment issued for nutrition purposes. Ref 9300/N. |
| brw-094 | A packed wort kettle, ready to install. | HEAVY. TWO PERSONNEL TO LIFT. ONE PROVIDED. |
| brw-095 | A packed cider press, ready to install. | Crate checked against manifest. Handle missing. Handle found under the bolts. |
| brw-096 | A packed fermenting vessel, ready to install. | Install against a bulkhead. Floor load limits apply. Proc 96. |
| brw-097 | A packed culture crock, ready to install. | CERAMIC. FRAGILE. BREAKAGE CHARGED TO RECEIVING STATION. |
| brw-098 | A packed pot still, ready to install. | Supplied for cleaning solvent recovery. Any other use is not the Company's knowledge. |
| brw-099 | A packed ageing rack, ready to install. | Time not included. Time is the operator's to provide. |
| brw-100 | A packed brew bottler, ready to install. | Delivered under Galley Provision Order 100. Bottles requisitioned separately. |
