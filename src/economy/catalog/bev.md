# Beverages — `bev`

The galley's drinks that are not brewed. Tea leaves from `veg` are cured and blended, green coffee from `frt` roasted
and ground, cocoa from `snk` whisked into milk, beans, oats, peas and rice ground into plant milks, fruit and vegetables pressed into juice, broths simmered, powders mixed
into electrolyte drinks; then served hot or iced in a cup, which leaves a dirty dish, or capped into bottles and filled
into pouches that keep. Every drink raises hydration and bladder; hot drinks and teas also ease stress, milks, shakes
and broths add a little satiety, juices a little immunity. Spent grounds and pulp go on to compost and feed; powders,
concentrates and syrups to the other galleys, the snacks and the brewers.

## Devices

| id | device | role | cells |
|---|---|---|---|
| bev.kettle | BV110 Kettle | galley | 1x1 |
| bev.brewer | BV220 Coffee Brewer | galley | 1x1 |
| bev.roaster | BV340 Bean Roaster | galley | 2x1 |
| bev.juicer | BV450 Juice Press | galley | 2x1 |
| bev.blender | BV160 Drink Blender | galley | 1x1 |
| bev.milker | BV580 Plant Milk Maker | galley | 2x1 |
| bev.brothpot | BV610 Broth Pot | galley | 2x1 |
| bev.capper | BV730 Drink Capper | galley | 1x1 |

## Items

| id | item | use | decays |
|---|---|---|---|
| bev-001 | Tea, Herbal | hydration +15, bladder +12, stress -5, leaves 1 cln-001 | 24 h → san-003 |
| bev-002 | Coffee, Hot | hydration +12, bladder +15, stress -3, fun +2, leaves 1 cln-001 | 24 h → san-003 |
| bev-003 | Juice, Fruit | hydration +15, bladder +12, satiety +3, immunity +1, leaves 1 cln-001 | 48 h → san-003 |
| bev-004 | Milk, Soy | hydration +12, bladder +10, satiety +5, fitness +1, leaves 1 cln-001 | 72 h → san-003 |
| bev-005 | Broth, Vegetable | hydration +15, bladder +10, satiety +4, stress -3, leaves 1 cln-001 | 48 h → san-003 |
| bev-006 | Drink, Electrolyte | hydration +20, bladder +10, health +1, leaves 1 cln-001 | 72 h → san-003 |
| bev-007 | Cocoa, Hot | hydration +12, bladder +10, satiety +4, stress -5, fun +3, leaves 1 cln-001 | 24 h → san-003 |
| bev-008 | Tea, Black | hydration +15, bladder +12, stress -5, leaves 1 cln-001 | 24 h → san-003 |
| bev-009 | Tea, Green | hydration +15, bladder +12, stress -5, immunity +1, leaves 1 cln-001 | 24 h → san-003 |
| bev-010 | Juice, Fruit, Bottled | hydration +25, bladder +18, satiety +3, immunity +1, leaves 1 pak-004 | 720 h → san-003 |
| bev-011 | Tea, Iced, Bottled | hydration +25, bladder +18, stress -3, leaves 1 pak-004 | 720 h → san-003 |
| bev-012 | Drink, Electrolyte, Bottled | hydration +25, bladder +15, health +1, leaves 1 pak-004 | — |
| bev-013 | Coffee, Pouched | hydration +20, bladder +18, stress -3, fun +2, leaves 1 pak-002 | — |
| bev-014 | Tea, Pouched | hydration +20, bladder +15, stress -4, leaves 1 pak-002 | — |
| bev-015 | Cocoa, Pouched | hydration +18, bladder +15, satiety +4, stress -4, fun +3, leaves 1 pak-002 | — |
| bev-016 | Juice, Pouched | hydration +20, bladder +15, satiety +3, immunity +1, leaves 1 pak-002 | — |
| bev-017 | Drink, Electrolyte, Pouched | hydration +25, bladder +12, health +1, leaves 1 pak-002 | — |
| bev-018 | Powder, Tea, Instant | — | — |
| bev-019 | Leaves, Tea, Black | — | — |
| bev-020 | Leaves, Tea, Green | — | — |
| bev-021 | Milk, Pea | hydration +12, bladder +10, satiety +5, fitness +1, leaves 1 cln-001 | 72 h → san-003 |
| bev-022 | Blend, Grain Coffee | — | — |
| bev-023 | Blend, Herbal Tea | — | — |
| bev-024 | Bag, Tea | — | — |
| bev-025 | Concentrate, Coffee | — | 168 h → san-003 |
| bev-026 | Beans, Coffee, Roasted | — | — |
| bev-027 | Coffee, Ground | — | — |
| bev-028 | Powder, Coffee, Instant | — | — |
| bev-029 | Grounds, Coffee, Spent | — | 120 h → san-003 |
| bev-030 | Filter, Coffee, Paper | — | — |
| bev-031 | Chicory, Roasted | — | — |
| bev-032 | Tea, Barley | hydration +15, bladder +12, stress -4, leaves 1 cln-001 | 24 h → san-003 |
| bev-033 | Cocoa, Spiced | hydration +12, bladder +10, satiety +4, stress -6, fun +3, leaves 1 cln-001 | 24 h → san-003 |
| bev-034 | Powder, Malted Milk | — | — |
| bev-035 | Broth, Lentil | hydration +15, bladder +10, satiety +6, stress -3, leaves 1 cln-001 | 48 h → san-003 |
| bev-036 | Mix, Cocoa, Instant | — | — |
| bev-037 | Powder, Electrolyte | — | — |
| bev-038 | Concentrate, Juice | — | — |
| bev-039 | Cordial, Berry | — | — |
| bev-040 | Syrup, Ginger | — | — |
| bev-041 | Pulp, Soy Milk | — | 48 h → san-003 |
| bev-042 | Milk, Oat | hydration +12, bladder +10, satiety +5, leaves 1 cln-001 | 72 h → san-003 |
| bev-043 | Milk, Rice | hydration +12, bladder +10, satiety +4, leaves 1 cln-001 | 72 h → san-003 |
| bev-044 | Powder, Plant Milk | — | — |
| bev-045 | Powder, Broth, Instant | — | — |
| bev-046 | Juice, Berry | hydration +15, bladder +12, satiety +2, immunity +2, leaves 1 cln-001 | 48 h → san-003 |
| bev-047 | Juice, Citrus | hydration +15, bladder +12, satiety +2, immunity +3, leaves 1 cln-001 | 48 h → san-003 |
| bev-048 | Juice, Melon | hydration +18, bladder +14, satiety +2, leaves 1 cln-001 | 48 h → san-003 |
| bev-049 | Juice, Tomato | hydration +15, bladder +12, satiety +3, immunity +1, leaves 1 cln-001 | 48 h → san-003 |
| bev-050 | Juice, Carrot | hydration +15, bladder +12, satiety +3, immunity +2, leaves 1 cln-001 | 48 h → san-003 |
| bev-051 | Juice, Green | hydration +15, bladder +12, immunity +3, toxin -1, leaves 1 cln-001 | 48 h → san-003 |
| bev-052 | Lemonade | hydration +15, bladder +12, fun +2, immunity +1, leaves 1 cln-001 | 72 h → san-003 |
| bev-053 | Cooler, Cucumber | hydration +18, bladder +12, stress -1, leaves 1 cln-001 | 48 h → san-003 |
| bev-054 | Punch, Fruit | hydration +15, bladder +12, satiety +2, fun +3, leaves 1 cln-001 | 48 h → san-003 |
| bev-055 | Soda, Fruit | hydration +12, bladder +14, fun +3, leaves 1 cln-001 | 24 h → san-003 |
| bev-056 | Lemonade, Sparkling | hydration +12, bladder +14, fun +4, immunity +1, leaves 1 cln-001 | 24 h → bev-052 |
| bev-057 | Soda, Spiced | hydration +12, bladder +14, fun +3, stress -1, leaves 1 cln-001 | 24 h → san-003 |
| bev-058 | Latte | hydration +12, bladder +14, satiety +3, stress -4, fun +2, leaves 1 cln-001 | 24 h → san-003 |
| bev-059 | Coffee, Grain | hydration +12, bladder +12, stress -3, fun +1, leaves 1 cln-001 | 24 h → san-003 |
| bev-060 | Chai | hydration +14, bladder +12, satiety +2, stress -5, fun +2, leaves 1 cln-001 | 24 h → san-003 |
| bev-061 | Milk, Golden | hydration +12, bladder +10, satiety +3, stress -5, pain -2, leaves 1 cln-001 | 24 h → san-003 |
| bev-062 | Milk, Spiced, Warm | hydration +12, bladder +10, satiety +3, stress -6, rest +2, leaves 1 cln-001 | 24 h → san-003 |
| bev-063 | Tea, Ginger Lemon | hydration +15, bladder +12, stress -4, immunity +2, leaves 1 cln-001 | 24 h → san-003 |
| bev-064 | Tea, Mint | hydration +15, bladder +12, stress -5, pain -1, leaves 1 cln-001 | 24 h → san-003 |
| bev-065 | Tea, Chamomile | hydration +15, bladder +12, stress -6, rest +2, leaves 1 cln-001 | 24 h → san-003 |
| bev-066 | Juice, Mulled | hydration +14, bladder +12, satiety +2, stress -5, fun +2, leaves 1 cln-001 | 24 h → san-003 |
| bev-067 | Tea, Iced | hydration +15, bladder +12, stress -3, fun +1, leaves 1 cln-001 | 24 h → san-003 |
| bev-068 | Coffee, Iced | hydration +12, bladder +15, stress -2, fun +2, leaves 1 cln-001 | 24 h → san-003 |
| bev-069 | Coffee, Cold Brew | hydration +12, bladder +15, stress -2, fun +2, leaves 1 cln-001 | 72 h → san-003 |
| bev-070 | Shake, Protein | hydration +10, bladder +8, satiety +10, fitness +3, leaves 1 cln-001 | 24 h → san-003 |
| bev-071 | Shake, Recovery | hydration +15, bladder +10, satiety +8, fitness +2, pain -2, leaves 1 cln-001 | 24 h → san-003 |
| bev-072 | Smoothie, Fruit | hydration +12, bladder +10, satiety +8, immunity +2, fun +2, leaves 1 cln-001 | 24 h → san-003 |
| bev-073 | Smoothie, Green | hydration +12, bladder +10, satiety +8, immunity +3, leaves 1 cln-001 | 24 h → san-003 |
| bev-074 | Milk, Soy, Chocolate | hydration +12, bladder +10, satiety +6, stress -2, fun +3, leaves 1 cln-001 | 72 h → san-003 |
| bev-075 | Milkshake, Soy | hydration +10, bladder +10, satiety +8, fun +4, leaves 1 cln-001 | 24 h → san-003 |
| bev-076 | Solution, Oral Rehydration | hydration +25, bladder +8, health +3, leaves 1 cln-001 | 72 h → san-003 |
| bev-077 | Broth, Mushroom | hydration +15, bladder +10, satiety +4, stress -3, immunity +1, leaves 1 cln-001 | 48 h → san-003 |
| bev-078 | Broth, Miso | hydration +15, bladder +10, satiety +4, stress -3, leaves 1 cln-001 | 48 h → san-003 |
| bev-079 | Broth, Algae | hydration +15, bladder +10, satiety +3, immunity +1, leaves 1 cln-001 | 48 h → san-003 |
| bev-080 | Milk, Soy, Bottled | hydration +25, bladder +18, satiety +6, fitness +1, leaves 1 pak-004 | 240 h → san-003 |
| bev-081 | Lemonade, Bottled | hydration +25, bladder +18, fun +2, immunity +1, leaves 1 pak-004 | 720 h → san-003 |
| bev-082 | Coffee, Cold Brew, Bottled | hydration +25, bladder +20, stress -2, fun +2, leaves 1 pak-004 | 720 h → san-003 |
| bev-083 | Soda, Fruit, Bottled | hydration +20, bladder +20, fun +4, leaves 1 pak-004 | — |
| bev-084 | Broth, Vegetable, Bottled | hydration +25, bladder +15, satiety +5, stress -3, leaves 1 pak-004 | 240 h → san-003 |
| bev-085 | Element, Heating, Kettle | fits bev.kettle | — |
| bev-086 | Basket, Filter, Coffee Brewer | fits bev.brewer | — |
| bev-087 | Drum, Bean Roaster | fits bev.roaster | — |
| bev-088 | Screen, Juice Press | fits bev.juicer | — |
| bev-089 | Blade Assembly, Drink Blender | fits bev.blender | — |
| bev-090 | Burr, Plant Milk Maker | fits bev.milker | — |
| bev-091 | Seal, Lid, Broth Pot | fits bev.brothpot | — |
| bev-092 | Crimp Head, Drink Capper | fits bev.capper | — |
| bev-093 | Kit, Kettle | installs bev.kettle | — |
| bev-094 | Kit, Coffee Brewer | installs bev.brewer | — |
| bev-095 | Kit, Bean Roaster | installs bev.roaster | — |
| bev-096 | Kit, Juice Press | installs bev.juicer | — |
| bev-097 | Kit, Drink Blender | installs bev.blender | — |
| bev-098 | Kit, Plant Milk Maker | installs bev.milker | — |
| bev-099 | Kit, Broth Pot | installs bev.brothpot | — |
| bev-100 | Kit, Drink Capper | installs bev.capper | — |

## Ways

| way | by | min | takes | makes | gives |
|---|---|---|---|---|---|
| wither and oxidise tea | bev.roaster | 120 | 3 veg-034, 1 pwr-001 | 2 bev-019 | — |
| steam and roll green tea | bev.roaster | 60 | 3 veg-034, 1 pwr-001 | 2 bev-020 | — |
| blend herbal tea | crew | 15 | 1 veg-072, 1 veg-073 | 2 bev-023 | — |
| fill tea bags | crew | 15 | 1 bev-019, 1 fib-064 | 4 bev-024 | — |
| brew and dry instant tea | bev.kettle | 90 | 2 bev-019, 2 wat-001, 2 pwr-001 | 3 bev-018 | — |
| roast coffee | bev.roaster | 45 | 3 frt-086, 1 pwr-001 | 3 bev-026 | — |
| grind coffee | crew | 10 | 2 bev-026 | 2 bev-027 | — |
| freeze-dry coffee | bev.brewer | 120 | 3 bev-027, 2 wat-001, 2 pwr-001 | 2 bev-028, 2 bev-029 | — |
| cold-drip coffee concentrate | bev.brewer | 240 | 2 bev-027, 2 wat-001 | 2 bev-025, 1 bev-029 | — |
| cut coffee filters | any.bench | 15 | 1 toi-056 | 6 bev-030 | — |
| roast root trimmings | bev.roaster | 45 | 3 veg-041, 1 pwr-001 | 2 bev-031 | — |
| blend grain coffee | bev.roaster | 30 | 1 grn-086, 1 bev-031 | 2 bev-022 | — |
| mix instant cocoa | any.bench | 10 | 1 snk-010, 1 ing-003, 1 bev-044 | 3 bev-036 | — |
| mix electrolyte powder | any.bench | 15 | 1 ing-002, 1 ing-003, 1 chm-065 | 4 bev-037 | — |
| reduce juice to concentrate | bev.brothpot | 90 | 4 bev-003, 2 pwr-001 | 1 bev-038, 4 cln-001 | — |
| simmer berry cordial | bev.brothpot | 60 | 2 frt-063, 1 ing-003, 1 pwr-001 | 2 bev-039 | — |
| simmer ginger syrup | bev.brothpot | 45 | 1 ing-057, 1 ing-003, 1 wat-001, 1 pwr-001 | 2 bev-040 | — |
| dry plant milk | bev.milker | 120 | 4 bev-004, 2 pwr-001 | 1 bev-044, 4 cln-001 | — |
| malt plant milk powder | bev.milker | 60 | 1 grn-058, 1 bev-044, 1 pwr-001 | 2 bev-034 | — |
| dry broth to powder | bev.brothpot | 120 | 4 bev-005, 2 pwr-001 | 1 bev-045, 4 cln-001 | — |
| steep herbal tea | bev.kettle | 10 | 1 bev-023, 2 wat-001, 2 cln-002, 1 pwr-001 | 2 bev-001, 1 san-002 | — |
| steep fresh mint | crew | 10 | 1 veg-030, 1 wat-006, 1 cln-002 | 1 bev-001 | — |
| brew black tea | bev.kettle | 10 | 1 bev-019, 2 wat-001, 2 cln-002, 1 pwr-001 | 2 bev-008, 1 san-002 | — |
| steep a tea bag | crew | 5 | 1 bev-024, 1 wat-006, 1 cln-002 | 1 bev-008 | — |
| brew green tea | bev.kettle | 10 | 1 bev-020, 2 wat-001, 2 cln-002, 1 pwr-001 | 2 bev-009, 1 san-002 | — |
| brew barley tea | bev.kettle | 15 | 1 grn-086, 2 wat-001, 2 cln-002, 1 pwr-001 | 2 bev-032, 1 san-002 | — |
| brew mint tea | bev.kettle | 10 | 1 veg-072, 2 wat-001, 2 cln-002, 1 pwr-001 | 2 bev-064, 1 san-002 | — |
| brew chamomile tea | bev.kettle | 10 | 1 veg-073, 2 wat-001, 2 cln-002, 1 pwr-001 | 2 bev-065, 1 san-002 | — |
| brew ginger lemon tea | bev.kettle | 10 | 1 bev-040, 1 frt-050, 2 wat-001, 2 cln-002, 1 pwr-001 | 2 bev-063 | — |
| brew chai | bev.kettle | 15 | 1 bev-019, 1 ing-004, 1 bev-044, 2 wat-001, 2 cln-002, 1 pwr-001 | 2 bev-060, 1 san-002 | — |
| warm golden milk | bev.kettle | 10 | 1 bev-044, 1 ing-004, 2 wat-001, 2 cln-002, 1 pwr-001 | 2 bev-061 | — |
| warm spiced milk | bev.kettle | 10 | 1 bev-034, 1 ing-004, 2 wat-001, 2 cln-002, 1 pwr-001 | 2 bev-062 | — |
| make hot cocoa | bev.kettle | 10 | 1 bev-036, 2 wat-001, 2 cln-002, 1 pwr-001 | 2 bev-007 | — |
| make spiced cocoa | bev.kettle | 10 | 1 bev-036, 1 ing-004, 2 wat-001, 2 cln-002, 1 pwr-001 | 2 bev-033 | — |
| mull juice | bev.kettle | 15 | 1 bev-038, 1 ing-004, 2 wat-001, 2 cln-002, 1 pwr-001 | 2 bev-066 | — |
| stir up instant broth | bev.kettle | 5 | 1 bev-045, 1 wat-006, 1 cln-002 | 1 bev-005 | — |
| brew filter coffee | bev.brewer | 10 | 1 bev-027, 1 bev-030, 2 wat-001, 2 cln-002, 1 pwr-001 | 2 bev-002, 1 bev-029 | — |
| stir instant coffee | crew | 3 | 1 bev-028, 1 wat-006, 1 cln-002 | 1 bev-002 | — |
| brew grain coffee | bev.brewer | 10 | 1 bev-022, 2 wat-001, 2 cln-002, 1 pwr-001 | 2 bev-059, 1 san-002 | — |
| pull a latte | bev.brewer | 10 | 1 bev-025, 1 bev-044, 2 wat-001, 2 cln-002, 1 pwr-001 | 2 bev-058 | — |
| pour iced coffee | bev.brewer | 5 | 1 bev-025, 1 wat-013, 1 wat-001, 2 cln-002 | 2 bev-068 | — |
| steep cold brew | bev.brewer | 480 | 2 bev-027, 3 wat-001, 3 cln-002 | 3 bev-069, 2 bev-029 | — |
| press mixed fruit | bev.juicer | 20 | 2 frt-002, 1 frt-004, 2 cln-002, 1 pwr-001 | 2 bev-003, 1 frt-009 | — |
| dilute juice concentrate | crew | 5 | 1 bev-038, 3 wat-001, 3 cln-002 | 3 bev-003 | — |
| press berry juice | bev.juicer | 20 | 3 frt-063, 2 cln-002, 1 pwr-001 | 2 bev-046, 1 frt-009 | — |
| press citrus juice | bev.juicer | 20 | 2 frt-004, 1 frt-005, 2 cln-002, 1 pwr-001 | 2 bev-047, 1 frt-010 | — |
| press melon juice | bev.juicer | 20 | 1 frt-008, 2 cln-002, 1 pwr-001 | 2 bev-048, 1 frt-031 | — |
| press tomato juice | bev.juicer | 20 | 3 veg-003, 2 cln-002, 1 pwr-001 | 2 bev-049, 1 san-002 | — |
| press carrot juice | bev.juicer | 20 | 3 veg-004, 2 cln-002, 1 pwr-001 | 2 bev-050, 1 san-002 | — |
| press green juice | bev.juicer | 20 | 2 veg-012, 1 veg-015, 1 frt-002, 2 cln-002, 1 pwr-001 | 2 bev-051, 1 san-002 | — |
| grind soy milk | bev.milker | 45 | 2 grn-081, 2 wat-001, 2 cln-002, 1 pwr-001 | 2 bev-004, 1 bev-041 | — |
| reconstitute plant milk | crew | 5 | 1 bev-044, 2 wat-001, 2 cln-002 | 2 bev-004 | — |
| grind pea milk | bev.milker | 45 | 2 veg-019, 2 wat-001, 2 cln-002, 1 pwr-001 | 2 bev-021, 1 bev-041 | — |
| grind oat milk | bev.milker | 45 | 2 grn-006, 2 wat-001, 2 cln-002, 1 pwr-001 | 2 bev-042, 1 san-002 | — |
| grind rice milk | bev.milker | 45 | 2 grn-003, 2 wat-001, 2 cln-002, 1 pwr-001 | 2 bev-043, 1 san-002 | — |
| simmer vegetable broth | bev.brothpot | 60 | 1 veg-065, 1 ing-002, 3 wat-001, 3 cln-002, 1 pwr-001 | 3 bev-005, 1 san-002 | — |
| thin vegetable stock | bev.brothpot | 20 | 1 ing-005, 2 wat-001, 2 cln-002, 1 pwr-001 | 2 bev-005 | — |
| simmer lentil broth | bev.brothpot | 90 | 1 grn-065, 1 ing-002, 3 wat-001, 3 cln-002, 1 pwr-001 | 3 bev-035 | — |
| simmer mushroom broth | bev.brothpot | 30 | 1 ing-014, 2 wat-001, 2 cln-002, 1 pwr-001 | 2 bev-077 | — |
| whisk miso broth | bev.brothpot | 10 | 1 ing-012, 2 wat-006, 2 cln-002 | 2 bev-078 | — |
| simmer algae broth | bev.brothpot | 30 | 1 ing-079, 2 wat-001, 2 cln-002, 1 pwr-001 | 2 bev-079 | — |
| mix an electrolyte drink | bev.blender | 5 | 1 bev-037, 2 wat-001, 2 cln-002, 1 pwr-001 | 2 bev-006 | — |
| mix oral rehydration solution | bev.blender | 5 | 1 bev-037, 1 ing-002, 2 wat-003, 2 cln-002, 1 pwr-001 | 2 bev-076 | — |
| mix lemonade | bev.blender | 5 | 1 frt-050, 1 ing-003, 2 wat-001, 2 cln-002, 1 pwr-001 | 2 bev-052 | — |
| blend a cucumber cooler | bev.blender | 5 | 2 veg-015, 2 wat-007, 2 cln-002, 1 pwr-001 | 2 bev-053 | — |
| mix fruit punch | bev.blender | 5 | 1 bev-038, 1 bev-039, 3 wat-001, 3 cln-002, 1 pwr-001 | 3 bev-054 | — |
| fizz a fruit soda | bev.blender | 5 | 1 bev-039, 2 wat-046, 2 cln-002, 1 pwr-001 | 2 bev-055 | — |
| fizz a sparkling lemonade | bev.blender | 5 | 1 frt-050, 1 ing-003, 2 wat-046, 2 cln-002, 1 pwr-001 | 2 bev-056 | — |
| fizz a spiced soda | bev.blender | 5 | 1 bev-040, 1 ing-004, 2 wat-046, 2 cln-002, 1 pwr-001 | 2 bev-057 | — |
| shake iced tea | bev.blender | 5 | 1 bev-018, 1 wat-013, 2 wat-001, 2 cln-002, 1 pwr-001 | 2 bev-067 | — |
| blend a protein shake | bev.blender | 5 | 1 prt-079, 1 bev-044, 2 wat-001, 2 cln-002, 1 pwr-001 | 2 bev-070 | — |
| blend a recovery shake | bev.blender | 5 | 1 prt-080, 1 frt-003, 1 bev-037, 2 wat-001, 2 cln-002, 1 pwr-001 | 2 bev-071 | — |
| blend a fruit smoothie | bev.blender | 5 | 1 frt-063, 1 frt-003, 1 bev-044, 1 wat-013, 2 cln-002, 1 pwr-001 | 2 bev-072 | — |
| blend a green smoothie | bev.blender | 5 | 1 veg-007, 1 frt-002, 1 bev-044, 1 wat-001, 2 cln-002, 1 pwr-001 | 2 bev-073 | — |
| blend chocolate soy milk | bev.blender | 5 | 1 bev-036, 1 bev-044, 2 wat-001, 2 cln-002, 1 pwr-001 | 2 bev-074 | — |
| blend a soy milkshake | bev.blender | 5 | 1 bev-034, 1 bev-044, 1 wat-013, 1 ing-003, 2 cln-002, 1 pwr-001 | 2 bev-075 | — |
| bottle fruit juice | bev.capper | 20 | 2 frt-002, 1 frt-004, 1 pak-003, 1 pwr-001 | 1 bev-010, 1 frt-009 | — |
| bottle iced tea | bev.capper | 20 | 1 bev-018, 2 wat-001, 1 ing-003, 1 pak-003, 1 pwr-001 | 1 bev-011 | — |
| bottle an electrolyte drink | bev.capper | 15 | 1 bev-037, 2 wat-001, 1 pak-003, 1 pwr-001 | 1 bev-012 | — |
| bottle soy milk | bev.capper | 15 | 1 bev-044, 2 wat-001, 1 pak-003, 1 pwr-001 | 1 bev-080 | — |
| bottle lemonade | bev.capper | 15 | 1 frt-050, 1 ing-003, 2 wat-001, 1 pak-003, 1 pwr-001 | 1 bev-081 | — |
| bottle cold brew | bev.capper | 15 | 1 bev-025, 1 wat-001, 1 pak-003, 1 pwr-001 | 1 bev-082 | — |
| bottle fruit soda | bev.capper | 15 | 1 bev-039, 2 wat-046, 1 pak-003, 1 pwr-001 | 1 bev-083 | — |
| bottle vegetable broth | bev.capper | 15 | 1 bev-045, 2 wat-006, 1 pak-003, 1 pwr-001 | 1 bev-084 | — |
| fill coffee drink pouches | bev.capper | 15 | 1 bev-028, 1 ing-003, 2 wat-001, 1 pak-001, 1 pwr-001 | 1 bev-013 | — |
| fill tea drink pouches | bev.capper | 15 | 1 bev-018, 2 wat-001, 1 pak-001, 1 pwr-001 | 1 bev-014 | — |
| fill cocoa drink pouches | bev.capper | 15 | 1 bev-036, 2 wat-001, 1 pak-001, 1 pwr-001 | 1 bev-015 | — |
| fill juice drink pouches | bev.capper | 15 | 1 bev-038, 2 wat-001, 1 pak-001, 1 pwr-001 | 1 bev-016 | — |
| fill electrolyte pouches | bev.capper | 15 | 1 bev-037, 2 wat-001, 1 pak-001, 1 pwr-001 | 1 bev-017 | — |
| make a kettle heating element | any.bench | 30 | 1 met-047, 1 cer-035 | 1 bev-085 | — |
| make a brewer filter basket | any.bench | 30 | 1 met-057 | 1 bev-086 | — |
| make a roaster drum | any.bench | 60 | 1 met-034, 1 mec-006 | 1 bev-087 | — |
| make a juicer press screen | any.bench | 30 | 1 met-034 | 1 bev-088 | — |
| make a blender blade assembly | any.bench | 45 | 1 met-049, 1 mec-004 | 1 bev-089 | — |
| grind a milk maker burr | any.bench | 60 | 1 met-030 | 1 bev-090 | — |
| cut broth pot lid seals | any.bench | 15 | 1 pol-036 | 2 bev-091 | — |
| make a capper crimp head | any.bench | 45 | 1 met-008, 1 mec-005 | 1 bev-092 | — |
| pack a kettle kit | any.bench | 90 | 1 fur-001, 1 bev-085, 1 met-034 | 1 bev-093 | — |
| pack a coffee brewer kit | any.bench | 90 | 1 fur-001, 1 bev-086, 1 thm-004 | 1 bev-094 | — |
| pack a bean roaster kit | any.bench | 120 | 1 fur-001, 1 bev-087, 1 mec-010 | 1 bev-095 | — |
| pack a juice press kit | any.bench | 120 | 1 fur-001, 1 bev-088, 1 mec-043 | 1 bev-096 | — |
| pack a drink blender kit | any.bench | 90 | 1 fur-001, 1 bev-089, 1 mec-010 | 1 bev-097 | — |
| pack a plant milk maker kit | any.bench | 120 | 1 fur-001, 1 bev-090, 1 mec-010, 1 thm-004 | 1 bev-098 | — |
| pack a broth pot kit | any.bench | 90 | 1 fur-001, 1 bev-091, 1 met-034, 1 thm-004 | 1 bev-099 | — |
| pack a drink capper kit | any.bench | 90 | 1 fur-001, 1 bev-092, 1 mec-043 | 1 bev-100 | — |
| mix lemonade with lime juice | bev.blender | 5 | 1 frt-051, 1 ing-003, 2 wat-001, 2 cln-002, 1 pwr-001 | 2 bev-052 | — |

## Codex

| id | about | flavour |
|---|---|---|
| bev.kettle | Boils water for teas, cocoa, chai, warm milks and mulled juice, and dries brewed tea to instant powder. | DO NOT BOIL DRY. ELEMENT REPLACEMENT CHARGED TO STATION. |
| bev.brewer | Brews filter, grain and cold brew coffee, pulls lattes and freeze-dries instant coffee. | Coffee is issued to sustain output. Any effect on morale is incidental. Ref 2207/G. |
| bev.roaster | Roasts coffee beans and root trimmings, cures tea leaves and blends grain coffee. | Drum rebalanced, rev 4. Smoke detector found disconnected by previous operator. Reconnected. |
| bev.juicer | Presses fruit and vegetables into juice, leaving pomace or scraps. | Pomace yield is audited. Short weight is recorded against the station. Ref 4410/J. |
| bev.blender | Mixes electrolyte drinks, rehydration solution, lemonades, sodas, shakes and smoothies. | LID SECURED BEFORE START. HANDS CLEAR OF JAR. |
| bev.milker | Grinds soybeans, peas, oats and rice into plant milk, and dries and malts milk powder. | No cows aboard. Someone still asks, every voyage. |
| bev.brothpot | Simmers broths, cordials and syrups, and reduces juice and broth to concentrate and powder. | May be left unattended per Proc 61. It requires no supervision and receives none. |
| bev.capper | Caps drinks into bottles and fills drink pouches for storage. | Every sealed unit is COF stock until consumed. Consumption is logged. |
| bev-001 | Mint and chamomile tea from the kettle, or fresh mint steeped by hand; a calming hot drink. | Herbal tea is not a medical treatment. Do not log it as one. Ref 1180/M. |
| bev-002 | Filter or instant coffee served hot in a cup; a mild stimulant with a small lift to morale. | Nothing gets fixed before the coffee. Nothing much after it either. |
| bev-003 | Mixed fruit juice served in a cup; slightly filling, supports immunity, and reduces to concentrate. | Pulp content varies by batch. Variance is within tolerance. Tolerance is not published. |
| bev-004 | Plant milk ground from soybeans or reconstituted from powder; filling, and a staple of the galley and the dairy vat. | SOY MILK. SHAKE BEFORE USE. COF GALLEY STOCK. |
| bev-005 | Simple vegetable broth, warming and calming; dries to powder for storage. | Approved for cold hands. Cold feet require Form 3C. |
| bev-006 | Electrolyte powder mixed in water; strong hydration with a small benefit to health. | Issue after exertion, fever or decontamination. Not after recreation. Proc 208. |
| bev-007 | Instant cocoa made hot; calming, slightly filling, with a small lift to morale. | Marshmallows are not a stocked item. Requests are filed and not answered. |
| bev-008 | Black tea brewed from leaves or a tea bag; a calming hot drink. | Milk in after. This is not a debate. |
| bev-009 | Green tea brewed from steamed leaves; calming, with mild immune support. | STEEP SHORT. BITTERNESS IS OPERATOR ERROR. |
| bev-010 | Fruit juice capped in a bottle for long storage; leaves an empty bottle. | Shelf life is guaranteed by the Company. The guarantee is not transferable. |
| bev-011 | Sweetened iced tea capped in a bottle for long storage; leaves an empty bottle. | Contents settle in transit. Invert once. Do not shake near panels. |
| bev-012 | Electrolyte drink capped in a bottle that does not spoil; leaves an empty bottle. | MEDKIT STOCK. REMOVAL FOR PERSONAL USE IS DEDUCTED. |
| bev-013 | Sweetened coffee sealed in a pouch that does not spoil; leaves an empty pouch. | Approved for consumption at the station. A break is not implied. Ref 0613/B. |
| bev-014 | Tea sealed in a pouch that does not spoil; leaves an empty pouch. | Lukewarm on issue, lukewarm on opening. Consistent, at least. |
| bev-015 | Cocoa sealed in a pouch that does not spoil; leaves an empty pouch. | Night shift allocation. Day shift consumption is a stock discrepancy. Form 15N. |
| bev-016 | Juice from concentrate sealed in a pouch that does not spoil; leaves an empty pouch. | RECONSTITUTED. FRUIT CONTENT NOT DECLARED. |
| bev-017 | Electrolyte drink sealed in a pouch that does not spoil; leaves an empty pouch. | Sip, do not gulp. Vomit in the air return is cleaned at the operator's cost. Proc 17. |
| bev-018 | Black tea brewed and dried to powder, for iced tea and tea pouches. | Add water. Adjust expectations to match. |
| bev-019 | Withered, oxidised tea leaves for black tea, chai, tea bags and kombucha. | Lot cured, sealed, weighed. Moisture check passed on second attempt. |
| bev-020 | Steamed and rolled tea leaves for green tea. | Sniffing stock is not a quality procedure. Discontinue. Ref 2020/T. |
| bev-021 | Plant milk ground from garden peas; filling, with a small benefit to fitness. | Green on the vine, white in the cup. Nobody has explained it to me. |
| bev-022 | Roasted barley and chicory blended as a coffee substitute. | Issued during bean shortfalls. Shortfalls are scheduled. Ref 2204/S. |
| bev-023 | Dried mint and chamomile blended for herbal tea. | BLEND RATIO PER GALLEY SPEC 23. DO NOT IMPROVISE. |
| bev-024 | Black tea in a muslin bag, steeped by hand in hot water. | One bag, one cup. Reuse is noted in the operator's file. |
| bev-025 | Cold-dripped coffee concentrate for lattes, iced coffee and bottled cold brew. | Not for consumption neat. Incident Report 2541 refers. |
| bev-026 | Roasted green coffee beans, ground by hand before brewing. | Roast date stamped on sack. Stamp illegible. Accepted anyway, rev 2. |
| bev-027 | Ground roast coffee for filter coffee, cold brew and freeze-drying. | Grind fresh. The voyage is long and nothing else is. |
| bev-028 | Freeze-dried coffee, stirred into hot water or filled into pouches. | INSTANT. FLAVOUR NOT WARRANTED. |
| bev-029 | Used coffee grounds for compost, worm bins, substrate and litter; spoils if stored. | Spent grounds remain Company property through every subsequent use. Ref 2900/C. |
| bev-030 | A single-use paper filter cut from pulp, for brewing filter coffee. | Single use. Paper does not grow on trees here. Nothing does. |
| bev-031 | Roasted root trimmings, blended into grain coffee. | Root waste reclassified as beverage stock under Directive 31. Savings recorded. |
| bev-032 | Roasted barley steeped into a nutty, calming tea. | Smells of toast. Nearest thing to a fireplace on this deck. |
| bev-033 | Hot cocoa with spice mix; more calming than plain cocoa. | Spice per cup is fixed. Additional spice is a requisition. Form 33S. |
| bev-034 | Malted barley and plant milk powder, for warm spiced milk and milkshakes. | MALTED. KEEP DRY. NOT A MEAL REPLACEMENT. |
| bev-035 | Thick split lentil broth; the most filling of the broths. | Spoon stood upright for four seconds. Logged as within spec. |
| bev-036 | Cocoa, sugar and milk powder mixed for hot cocoa, cocoa pouches and chocolate milk. | Sugar content is reviewed annually. Review postponed. Ref 3606/Q. |
| bev-037 | Salt, sugar and citric acid mixed for electrolyte drinks, shakes and rehydration. | Tastes of sweat. Possibly by design. |
| bev-038 | Reduced fruit juice for diluting, punch, mulled juice, pouches and gummies. | STICKY. WIPE SPILLS FROM CONSOLES AT ONCE. |
| bev-039 | Simmered berry syrup for sodas, punch, lollipops and fermented soda. | Dilution ratio per label. Label removed by previous operator. |
| bev-040 | A sweet, spicy syrup for ginger lemon tea, spiced soda, ginger beer and hot toddies. | Ginger is classed as a condiment, not a remedy. Claims otherwise are unsupported. Ref 4012. |
| bev-041 | Wet pulp left from grinding soy or pea milk, sent to compost. | Batch residue, inspected. Destination: compost. Appeal: none. |
| bev-042 | Plant milk ground from rolled oats; filling, and used in oat batter. | OAT MILK. STIR BEFORE USE. SEPARATION IS NORMAL. |
| bev-043 | Plant milk ground from rice; mild and slightly filling. | No complaints on file. No compliments either. Ref 4300/R. |
| bev-044 | Dried soy milk for storage, used in lattes, cocoa, shakes, chai and milk chocolate. | Reconstitute with drinking water only. Raw water voids the product warranty. Proc 44. |
| bev-045 | Dried vegetable broth, stirred up hot or bottled. | SOUP BASE. ONE SCOOP PER CUP. SCOOP NOT SUPPLIED. |
| bev-046 | Pressed mixed berry juice; supports immunity. | Stains on coveralls are deducted at laundry cost. Berry stains doubly. Ref 4602. |
| bev-047 | Pressed mandarin and lemon juice; the strongest juice for immunity. | Scurvy is a preventable absence. Absence is unpaid. Notice 47/V. |
| bev-048 | Pressed melon juice; strongly hydrating. | Mostly water. Counted against the water ration anyway. |
| bev-049 | Pressed tomato juice; slightly filling. | Classed as a beverage for ration purposes and as a food for audit purposes. |
| bev-050 | Pressed carrot juice; supports immunity. | Good for eyesight, the old manuals say. Eye tests remain mandatory. Proc 50. |
| bev-051 | Kale, cucumber and apple juice; supports immunity and reduces toxin. | Tastes like it is working. Hope that it is. |
| bev-052 | Lemon or lime juice with sugar and water; a light recreational drink, also mixed into shandy. | LEMONADE. LIME SUBSTITUTION AUTHORISED. NAME RETAINED. |
| bev-053 | Cucumber blended with chilled water; strongly hydrating. | Chilled water is drawn from cabin reserve. Each draw is logged on Form 53C. |
| bev-054 | Juice concentrate and berry cordial in water; a drink for occasions. | Communal vessels are not issued. Punch is served by the cup. Ref 5400/P. |
| bev-055 | Berry cordial in sparkling water; a recreational drink that goes flat quickly. | Carbonation decays on schedule. So does everything here. |
| bev-056 | Lemonade made with sparkling water; goes flat into plain lemonade. | Loss of carbonation does not constitute spoilage. Claims refused. Ref 5611. |
| bev-057 | Ginger syrup and spice in sparkling water; a recreational drink. | PRESSURISED. OPEN AWAY FROM FACE AND INSTRUMENTS. |
| bev-058 | Coffee concentrate with plant milk; calming and slightly filling. | Foam art is not a job function. Time spent on it is logged. |
| bev-059 | Brewed grain coffee blend; a coffee substitute that contains no coffee. | Not coffee. Do not tell the machine. |
| bev-060 | Black tea, spice and milk powder brewed together; calming and warming. | Spice ratio per Galley Spec 60. Deviations are noted and tolerated. |
| bev-061 | Spiced warm plant milk that soothes and eases pain. | Turmeric residue does not wash out of cups. Cup replacement is chargeable. |
| bev-062 | Malted milk warmed with spice; calming, and it aids rest. | Drink it and the night shift ends sooner. It does not. |
| bev-063 | Ginger syrup and lemon juice in hot water; supports immunity. | Sick leave requires Form 63A countersigned by medbay. Drink this instead. |
| bev-064 | Dried mint tea; calming, and eases minor pain. | MINT. CLEARS SINUSES. DOES NOT CLEAR FILTERS. |
| bev-065 | Chamomile tea that calms and aids rest. | Issued to reduce sleep debt. Sleep debt remains the operator's liability. |
| bev-066 | Hot spiced juice; calming, with a small lift to morale. | Non-alcoholic by regulation. Seasonal by nothing; there are no seasons. |
| bev-067 | Instant tea shaken over ice; a cool, mildly calming drink. | Ice drawn from cabin stock. The rattle is the best part. |
| bev-068 | Coffee concentrate poured over ice and water. | ICED. SERVE COLD. NOT A HEAT SINK. |
| bev-069 | Ground coffee steeped cold and slow; keeps longer than hot coffee. | Steep cycle exceeds one shift. Handover of the brewer is mandatory. Proc 69. |
| bev-070 | Protein powder blended with plant milk; filling, and builds fitness. | Fitness is a contract condition. This is how it is met. |
| bev-071 | Recovery protein, banana and electrolytes blended; taken after training, and eases pain. | Sore today. Scheduled anyway tomorrow. |
| bev-072 | Berries, banana and plant milk blended over ice; filling, recreational and supports immunity. | Fruit allocation consumed in liquid form is still consumed. Ref 7202/F. |
| bev-073 | Spinach, apple and plant milk blended; filling and supports immunity. | Drink it fast, before it settles into layers. |
| bev-074 | Cocoa mix blended into plant milk; filling and recreational. | CHOCOLATE FLAVOURED. COCOA CONTENT BELOW DECLARATION THRESHOLD. |
| bev-075 | Malted milk, sugar and ice blended thick; filling and recreational. | Straw failure is not a defect of the shake. Straw complaints to Form 75K. |
| bev-076 | Electrolytes and salt in distilled water; the strongest rehydration, with a benefit to health. | MEDICAL ISSUE. DISTILLED WATER ONLY. NOT FOR FLAVOUR. |
| bev-077 | Mushroom stock simmered into broth; calming, with mild immune support. | Grown in the dark, served in the dark. Lighting reduced, rev 9. |
| bev-078 | Miso whisked into hot water; a quick, calming broth. | Stir until the clouds settle. They never fully do. |
| bev-079 | Algae stock simmered into broth; mild immune support. | Meets Minimum Nutrition Standard 79. Taste is not a standard. |
| bev-080 | Soy milk capped in a bottle for medium-term storage; leaves an empty bottle. | SHAKE WELL. CONTENTS SEPARATE. |
| bev-081 | Lemonade capped in a bottle for long storage; leaves an empty bottle. | Sour enough to go through the door slot for something sweet. |
| bev-082 | Cold brew coffee capped in a bottle for long storage; leaves an empty bottle. | Transfers of stimulants between stations are not tracked and not condoned. Notice 82/D. |
| bev-083 | Fruit soda capped in a bottle that holds its carbonation; leaves an empty bottle. | Cap under pressure. Open away from instruments. Ref 8303. |
| bev-084 | Broth made from powder and capped in a bottle for storage; leaves an empty bottle. | Hot meal substitute, issued cold. Reheating is at the station's own power cost. |
| bev-085 | A replacement heating element fitted to the kettle. | Coil reseated, continuity tested, rev 3. Scale buildup noted and ignored. |
| bev-086 | A replacement filter basket fitted to the coffee brewer. | MESH BASKET. RINSE AFTER EACH CYCLE. |
| bev-087 | A replacement drum fitted to the bean roaster. | Bearings greased, rev 5. Smells of every roast before it. |
| bev-088 | A replacement press screen fitted to the juice press. | Screen tears are recorded as operator wear, not part failure. Ref 8812. |
| bev-089 | A replacement blade assembly fitted to the drink blender. | DO NOT TEST WITH FINGERS. COF ACCEPTS NO LIABILITY. |
| bev-090 | A replacement grinding burr fitted to the plant milk maker. | Burr gap set to spec. Grinds beans fine and patience finer. |
| bev-091 | A replacement lid seal fitted to the broth pot. | Keeps the steam in. The smell gets out regardless. |
| bev-092 | A replacement crimp head fitted to the drink capper. | Calibrated to tolerance, rev 6. Inspector's stamp smudged. |
| bev-093 | A packed kettle, ready to install. | ASSEMBLY BY STATION PERSONNEL. INSTRUCTIONS NOT INCLUDED. |
| bev-094 | A packed coffee brewer, ready to install. | Installation time counts toward the shift, not against it. Ref 9401/K. |
| bev-095 | A packed bean roaster, ready to install. | Crate opened, contents counted, one bolt short. As usual. |
| bev-096 | A packed juice press, ready to install. | Kits unpacked outside an assigned station lose warranty cover. Form 96W. |
| bev-097 | A packed drink blender, ready to install. | Packing slip signed, crate resealed, tape reused twice. |
| bev-098 | A packed plant milk maker, ready to install. | Dispatched under Galley Provision Order 98. Delivery date is the delivery date. |
| bev-099 | A packed broth pot, ready to install. | COF GALLEY EQUIPMENT. SERIAL ON BASE. DO NOT REMOVE PLATE. |
| bev-100 | A packed drink capper, ready to install. | Turns drinks into stock. Stock belongs to the Company. |
