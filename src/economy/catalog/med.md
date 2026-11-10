# Medicines — `med`

Every remedy taken by mouth, on the skin or by needle: painkillers, antibiotics, antivirals, vitamins, sedatives,
anxiolytics, sleeping pills and antidotes. Herbs from the capsule's own pots, chemicals and cultures become active
powders; powders are pressed, filled, compounded or sealed into tablets, capsules, syrups, ointments and ampoules. The
strong ones bite back — a sedative calms and dulls, a nerve block numbs and weakens. Medicines expire into an expired
form that the disposal unit ends; their blister packs, vials, tubes and bottles go back to `pak`.

## Devices

| id | device | role | cells |
|---|---|---|---|
| med.reactor | PX400 Synthesis Reactor | chem | 2x2 |
| med.extractor | PX210 Herb Extractor | chem | 2x1 |
| med.fermenter | PX300 Culture Fermenter | med | 2x2 |
| med.press | PX100 Tablet Press | med | 2x1 |
| med.compounder | PX150 Compounding Hood | med | 2x1 |
| med.disposal | PX900 Drug Disposal Unit | chem | 1x1 |

## Items

| id | item | use | decays |
|---|---|---|---|
| med-001 | Tablet, Painkiller | pain -30, toxin +2, leaves 1 pak-018 | 1440 h → med-049 |
| med-002 | Tablet, Antibiotic | health +15, immunity +10, bowel +8, leaves 1 pak-018 | 1080 h → med-049 |
| med-003 | Tablet, Vitamin | immunity +5, leaves 1 pak-018 | 2160 h → med-049 |
| med-004 | Tablet, Sedative | stress -25, fitness -5, fun -5, leaves 1 pak-018 | 1440 h → med-049 |
| med-005 | Pill, Sleeping | rest +20, stress -5, fun -5, leaves 1 pak-018 | 1440 h → med-049 |
| med-006 | Tablet, Anxiolytic | stress -15, fun -3, leaves 1 pak-018 | 1440 h → med-049 |
| med-007 | Capsule, Antiviral | immunity +20, health +8, toxin +3, leaves 1 pak-018 | 1080 h → med-049 |
| med-008 | Solution, Antiseptic | health +5, immunity +5, pain +3, leaves 1 pak-004 | 2160 h → med-050 |
| med-009 | Tablet, Anti-Inflammatory | pain -15, health +5, toxin +2, leaves 1 pak-018 | 1440 h → med-049 |
| med-010 | Tablet, Antiemetic | toxin -10, health +3, leaves 1 pak-018 | 1440 h → med-049 |
| med-011 | Ampoule, Vaccine | immunity +40, pain +5, leaves 1 pak-020 | 480 h → med-051 |
| med-012 | Ampoule, Nerve Block | pain -60, fitness -5, leaves 1 pak-020 | 1080 h → med-051 |
| med-013 | Salts, Oral Rehydration | hydration +15, bladder +10, toxin -3, leaves 1 pak-016 | — |
| med-014 | Tablet, Charcoal Detox | toxin -15, bowel +5, leaves 1 pak-018 | — |
| med-015 | Tablet, Antihistamine | immunity +5, health +3, fitness -2, leaves 1 pak-018 | 1440 h → med-049 |
| med-016 | Syrup, Cough | pain -5, health +5, rest +5, leaves 1 pak-004 | 720 h → med-050 |
| med-017 | Ointment, Burn | pain -10, health +8, leaves 1 pak-012 | 1440 h → med-052 |
| med-018 | Balm, Muscle | pain -10, fitness +2, leaves 1 pak-012 | 1440 h → med-052 |
| med-019 | Cream, Antifungal | health +6, hygiene +3, leaves 1 pak-012 | 1440 h → med-052 |
| med-020 | Ointment, Antibiotic | health +8, immunity +3, leaves 1 pak-012 | 1440 h → med-052 |
| med-021 | Drops, Eye | health +3, pain -3, leaves 1 pak-004 | 720 h → med-050 |
| med-022 | Lozenge, Throat | pain -5, health +2 | 2160 h → med-049 |
| med-023 | Tablet, Fever Reducer | pain -10, health +6, leaves 1 pak-018 | 1440 h → med-049 |
| med-024 | Sachet, Cold and Flu | health +8, pain -10, rest +5, leaves 1 pak-016 | 1440 h → med-049 |
| med-025 | Tablet, Antacid | pain -5, toxin -3, leaves 1 pak-018 | 2160 h → med-049 |
| med-026 | Capsule, Probiotic, Gut | immunity +5, toxin -3, leaves 1 pak-018 | 720 h → med-049 |
| med-027 | Tablet, Iron Supplement | health +4, fitness +2, leaves 1 pak-018 | 2160 h → med-049 |
| med-028 | Tablet, Bone Density | fitness +5, health +2, leaves 1 pak-018 | 2160 h → med-049 |
| med-029 | Capsule, Vitamin D | immunity +3, fitness +3, leaves 1 pak-018 | 2160 h → med-049 |
| med-030 | Syrup, Multivitamin | immunity +6, leaves 1 pak-004 | 720 h → med-050 |
| med-031 | Drops, Calming, Herbal | stress -8, leaves 1 pak-004 | 1440 h → med-050 |
| med-032 | Tincture, Sleep, Valerian | rest +8, stress -5, fun -2, leaves 1 pak-004 | 1440 h → med-050 |
| med-033 | Ampoule, Antidote | toxin -40, pain +5, leaves 1 pak-020 | 1080 h → med-051 |
| med-034 | Ampoule, Tranquilliser | stress -40, rest +10, fitness -10, fun -10, leaves 1 pak-020 | 1080 h → med-051 |
| med-035 | Draught, Sleeping | rest +30, stress -10, fitness -5, fun -5, toxin +3, leaves 1 pak-004 | 720 h → med-050 |
| med-036 | Tablet, Muscle Relaxant | pain -15, stress -10, fitness -5, leaves 1 pak-018 | 1440 h → med-049 |
| med-037 | Tablet, Mood Stabiliser | stress -12, fun +3, toxin +2, leaves 1 pak-018 | 1440 h → med-049 |
| med-038 | Tablet, Migraine | pain -25, stress -5, rest -3, leaves 1 pak-018 | 1440 h → med-049 |
| med-039 | Ampoule, Antiviral | immunity +25, health +10, pain +3, leaves 1 pak-020 | 1080 h → med-051 |
| med-040 | Ampoule, Antibiotic | health +25, immunity +10, bowel +8, pain +3, leaves 1 pak-020 | 1080 h → med-051 |
| med-041 | Shot, Immune Booster | immunity +20, pain +3, leaves 1 pak-020 | 720 h → med-051 |
| med-042 | Gel, Anaesthetic, Local | pain -20, fitness -2, leaves 1 pak-012 | 1440 h → med-052 |
| med-043 | Tablet, Painkiller, Strong | pain -45, stress -5, fitness -3, toxin +5, leaves 1 pak-018 | 1440 h → med-049 |
| med-044 | Gel, Burn, Aloe | pain -8, health +4, leaves 1 pak-012 | 480 h → med-052 |
| med-045 | Capsule, Liver Support | toxin -10, health +3, leaves 1 pak-018 | 2160 h → med-049 |
| med-046 | Tonic, Immune, Herbal | immunity +8, leaves 1 pak-004 | 720 h → med-050 |
| med-047 | Lotion, Anti-Itch | stress -3, pain -3, health +2, leaves 1 pak-004 | 1440 h → med-050 |
| med-048 | Tablet, Decongestant | health +4, rest -3, stress +2, leaves 1 pak-018 | 1440 h → med-049 |
| med-049 | Medicine, Dry, Expired | — | — |
| med-050 | Medicine, Liquid, Expired | — | — |
| med-051 | Ampoule, Expired | — | — |
| med-052 | Ointment, Expired | — | — |
| med-053 | Tonic, Recovery | health +15, immunity +5, fitness +2, leaves 1 pak-004 | 720 h → med-050 |
| med-054 | Tablet, Cortisone | pain -20, health +5, immunity -5, leaves 1 pak-018 | 1440 h → med-049 |
| med-055 | Salve, Wound Healing | health +12, pain -5, leaves 1 pak-012 | 1440 h → med-052 |
| med-056 | Bark, Willow | — | — |
| med-057 | Root, Valerian | — | 240 h |
| med-058 | Flower, Echinacea | — | 168 h |
| med-059 | Powder, Salicylate | — | — |
| med-060 | Powder, Analgesic | — | — |
| med-061 | Powder, Anti-Inflammatory | — | — |
| med-062 | Powder, Sedative | — | — |
| med-063 | Powder, Anxiolytic | — | — |
| med-064 | Powder, Hypnotic | — | — |
| med-065 | Broth, Antibiotic, Mould | — | 72 h |
| med-066 | Powder, Antibiotic | — | — |
| med-067 | Powder, Antiviral | — | — |
| med-068 | Culture, Vaccine Antigen | — | 120 h |
| med-069 | Powder, Antihistamine | — | — |
| med-070 | Powder, Antiemetic | — | — |
| med-071 | Concentrate, Vitamin | — | — |
| med-072 | Powder, Calcium Supplement | — | — |
| med-073 | Powder, Iron Supplement | — | — |
| med-074 | Powder, Charcoal, Medicinal | — | — |
| med-075 | Powder, Anaesthetic | — | — |
| med-076 | Powder, Antidote | — | — |
| med-077 | Powder, Antifungal | — | — |
| med-078 | Powder, Probiotic | — | 720 h |
| med-079 | Base, Tincture, Herbal | — | — |
| med-080 | Extract, Aloe, Medicinal | — | 240 h |
| med-081 | Concentrate, Antiseptic | — | — |
| med-082 | Powder, Cough Suppressant | — | — |
| med-083 | Binder, Tablet | — | — |
| med-084 | Shell, Capsule, Gelatin | — | — |
| med-085 | Base, Syrup, Medicine | — | — |
| med-086 | Base, Ointment | — | — |
| med-087 | Diluent, Sterile | — | — |
| med-088 | Spray, Nasal, Saline | health +3, immunity +2, leaves 1 pak-028 | 1440 h → med-050 |
| med-089 | Stirrer Seal, Synthesis Reactor | fits med.reactor | 1500 h → scr-004 |
| med-090 | Mesh Screen, Herb Extractor | fits med.extractor | 1000 h → scr-001 |
| med-091 | Air Filter, Culture Fermenter | fits med.fermenter | 720 h → scr-004 |
| med-092 | Die Set, Tablet Press | fits med.press | 2000 h → scr-001 |
| med-093 | Filter, Compounding Hood | fits med.compounder | 720 h → scr-004 |
| med-094 | Nozzle, Drug Disposal Unit | fits med.disposal | 1500 h → scr-001 |
| med-095 | Kit, Synthesis Reactor | installs med.reactor | — |
| med-096 | Kit, Herb Extractor | installs med.extractor | — |
| med-097 | Kit, Culture Fermenter | installs med.fermenter | — |
| med-098 | Kit, Tablet Press | installs med.press | — |
| med-099 | Kit, Compounding Hood | installs med.compounder | — |
| med-100 | Kit, Drug Disposal Unit | installs med.disposal | — |

## Ways

| way | by | min | takes | makes | gives |
|---|---|---|---|---|---|
| extract willow salicylate | med.extractor | 90 | 2 med-056, 1 chm-004, 1 pwr-001 | 2 med-059 | — |
| synthesise salicylate | med.reactor | 120 | 1 chm-036, 1 chm-029, 1 pwr-001 | 2 med-059 | — |
| synthesise analgesic | med.reactor | 120 | 1 chm-036, 1 chm-008, 1 chm-029, 1 pwr-001 | 2 med-060 | — |
| synthesise anti-inflammatory | med.reactor | 90 | 1 med-059, 1 chm-029, 1 pwr-001 | 2 med-061 | — |
| synthesise sedative | med.reactor | 150 | 1 chm-020, 1 chm-004, 1 pwr-001 | 1 med-062 | — |
| extract valerian sedative | med.extractor | 120 | 2 med-057, 1 chm-004, 1 pwr-001 | 1 med-062 | — |
| synthesise anxiolytic | med.reactor | 150 | 1 chm-003, 1 chm-009, 1 chm-033, 1 pwr-001 | 1 med-063 | — |
| synthesise hypnotic | med.reactor | 120 | 1 med-062, 1 chm-009, 1 pwr-001 | 1 med-064 | — |
| extract chamomile hypnotic | med.extractor | 120 | 2 veg-073, 1 med-057, 1 chm-004, 1 pwr-001 | 1 med-064 | — |
| brew mould broth | med.fermenter | 480 | 1 san-003, 1 grn-062, 1 wat-003, 1 pwr-001 | 2 med-065 | — |
| purify antibiotic | med.reactor | 120 | 2 med-065, 1 chm-033, 1 pwr-001 | 1 med-066 | — |
| synthesise antiviral | med.reactor | 180 | 1 chm-022, 1 chm-003, 1 chm-030, 1 pwr-001 | 1 med-067 | — |
| grow vaccine antigen | med.fermenter | 720 | 1 bio-070, 1 bio-009, 1 pwr-001 | 2 med-068 | — |
| synthesise antihistamine | med.reactor | 120 | 1 chm-036, 1 chm-003, 1 pwr-001 | 1 med-069 | — |
| extract mint antiemetic | med.extractor | 90 | 2 veg-030, 1 chm-004, 1 pwr-001 | 1 med-070 | — |
| synthesise antiemetic | med.reactor | 120 | 1 chm-009, 1 chm-034, 1 pwr-001 | 1 med-070 | — |
| extract algae vitamins | med.extractor | 90 | 2 prt-031, 1 chm-004, 1 pwr-001 | 2 med-071 | — |
| ferment yeast vitamins | med.fermenter | 360 | 1 bio-009, 1 ing-003, 1 pwr-001 | 1 med-071 | — |
| refine calcium powder | med.reactor | 60 | 1 chm-067, 1 pwr-001 | 2 med-072 | — |
| grind eggshell calcium | any.bench | 45 | 2 soi-047 | 1 med-072 | — |
| make iron supplement | med.reactor | 90 | 1 met-060, 1 chm-001, 1 pwr-001 | 2 med-073 | — |
| wash medicinal charcoal | med.reactor | 60 | 1 chm-005, 1 wat-003, 1 pwr-001 | 2 med-074 | — |
| char rice hulls | any.bench | 90 | 2 grn-038, 1 pwr-001 | 1 med-074 | — |
| synthesise anaesthetic | med.reactor | 150 | 1 chm-004, 1 chm-008, 1 chm-036, 1 pwr-001 | 1 med-075 | — |
| synthesise antidote | med.reactor | 120 | 1 chm-063, 1 chm-048, 1 pwr-001 | 1 med-076 | — |
| synthesise antifungal | med.reactor | 120 | 1 chm-006, 1 chm-036, 1 pwr-001 | 1 med-077 | — |
| ferment probiotics | med.fermenter | 360 | 1 bio-010, 1 ing-003, 1 pwr-001 | 2 med-078 | — |
| tincture echinacea | med.extractor | 120 | 1 med-058, 1 chm-004, 1 pwr-001 | 2 med-079 | — |
| tincture dried herbs | med.extractor | 120 | 2 veg-071, 1 chm-004, 1 pwr-001 | 1 med-079 | — |
| extract aloe | med.extractor | 60 | 2 veg-069, 1 pwr-001 | 1 med-080 | — |
| squeeze aloe leaves | any.bench | 30 | 2 veg-036 | 1 med-080 | — |
| dissolve iodine antiseptic | med.reactor | 60 | 1 chm-039, 1 chm-004, 1 pwr-001 | 2 med-081 | — |
| dilute peroxide antiseptic | med.compounder | 30 | 1 chm-007, 1 wat-003 | 1 med-081 | — |
| extract menthol | med.extractor | 90 | 2 veg-072, 1 chm-004, 1 pwr-001 | 1 med-082 | — |
| synthesise cough suppressant | med.reactor | 120 | 1 chm-010, 1 chm-036, 1 pwr-001 | 1 med-082 | — |
| mix tablet binder | med.compounder | 30 | 1 grn-066, 1 chm-064, 1 pwr-001 | 3 med-083 | — |
| knead starch binder | any.bench | 30 | 1 grn-062, 1 wat-001 | 2 med-083 | — |
| cast fish gelatin shells | med.compounder | 60 | 1 prt-050, 1 wat-003, 1 pwr-001 | 4 med-084 | — |
| cast plant capsule shells | med.compounder | 60 | 1 grn-066, 1 bio-068, 1 pwr-001 | 4 med-084 | — |
| cook syrup base | med.compounder | 30 | 1 ing-003, 1 wat-003, 1 pwr-001 | 2 med-085 | — |
| boil syrup by hand | any.bench | 45 | 1 ing-003, 1 wat-001, 1 pwr-001 | 1 med-085 | — |
| blend wax ointment base | med.compounder | 40 | 1 pol-067, 1 ing-001, 1 pwr-001 | 2 med-086 | — |
| blend silicone ointment base | med.compounder | 40 | 1 chm-064, 1 pol-074, 1 pwr-001 | 2 med-086 | — |
| mix sterile diluent | med.compounder | 30 | 1 wat-029, 1 ing-002, 1 pwr-001 | 2 med-087 | — |
| boil saline diluent | med.compounder | 60 | 1 wat-003, 1 ing-002, 2 pwr-001 | 1 med-087 | — |
| press painkillers | med.press | 60 | 1 med-060, 1 med-083, 2 pak-017, 1 pwr-001 | 2 med-001 | — |
| press salicylate painkillers | med.press | 60 | 1 med-059, 1 med-083, 2 pak-017, 1 pwr-001 | 2 med-001 | — |
| press antibiotic tablets | med.press | 60 | 1 med-066, 1 med-083, 2 pak-017, 1 pwr-001 | 2 med-002 | — |
| press vitamin tablets | med.press | 60 | 1 med-071, 1 med-083, 2 pak-017, 1 pwr-001 | 2 med-003 | — |
| hand-press vitamin tablets | any.bench | 60 | 2 med-071, 1 med-083, 1 pak-017 | 1 med-003 | — |
| press sedative tablets | med.press | 60 | 1 med-062, 1 med-083, 2 pak-017, 1 pwr-001 | 2 med-004 | — |
| press sleeping pills | med.press | 60 | 1 med-064, 1 med-083, 2 pak-017, 1 pwr-001 | 2 med-005 | — |
| press anxiolytic tablets | med.press | 60 | 1 med-063, 1 med-083, 2 pak-017, 1 pwr-001 | 2 med-006 | — |
| fill antiviral capsules | med.press | 60 | 1 med-067, 2 med-084, 2 pak-017, 1 pwr-001 | 2 med-007 | — |
| bottle antiseptic | med.compounder | 30 | 1 med-081, 1 wat-003, 1 pak-003 | 1 med-008 | — |
| bottle alcohol antiseptic | med.compounder | 30 | 1 chm-034, 1 wat-003, 1 pak-003 | 1 med-008 | — |
| press anti-inflammatory tablets | med.press | 60 | 1 med-061, 1 med-083, 2 pak-017, 1 pwr-001 | 2 med-009 | — |
| press antiemetic tablets | med.press | 60 | 1 med-070, 1 med-083, 2 pak-017, 1 pwr-001 | 2 med-010 | — |
| seal vaccine ampoules | med.compounder | 60 | 1 med-068, 1 med-087, 1 pak-019, 1 pwr-001 | 1 med-011 | — |
| seal nerve block ampoules | med.compounder | 60 | 1 med-075, 1 med-087, 1 pak-019, 1 pwr-001 | 1 med-012 | — |
| mix rehydration salts | med.compounder | 15 | 2 ing-002, 2 ing-003, 2 pak-015, 1 pwr-001 | 2 med-013 | — |
| mix rehydration salts by hand | any.bench | 30 | 1 ing-002, 1 ing-003, 1 pak-015 | 1 med-013 | — |
| press charcoal tablets | med.press | 60 | 1 med-074, 1 med-083, 2 pak-017, 1 pwr-001 | 2 med-014 | — |
| press antihistamine tablets | med.press | 60 | 1 med-069, 1 med-083, 2 pak-017, 1 pwr-001 | 2 med-015 | — |
| compound cough syrup | med.compounder | 45 | 1 med-082, 1 med-085, 1 pak-003, 1 pwr-001 | 1 med-016 | — |
| compound burn ointment | med.compounder | 40 | 1 med-081, 1 med-086, 1 pak-011 | 1 med-017 | — |
| compound muscle balm | med.compounder | 40 | 1 med-059, 1 med-086, 1 pak-011 | 1 med-018 | — |
| compound antifungal cream | med.compounder | 40 | 1 med-077, 1 med-086, 1 pak-011 | 1 med-019 | — |
| compound antibiotic ointment | med.compounder | 40 | 1 med-066, 1 med-086, 1 pak-011 | 1 med-020 | — |
| compound eye drops | med.compounder | 30 | 1 med-069, 1 med-087, 1 pak-003 | 1 med-021 | — |
| press throat lozenges | med.press | 45 | 1 med-082, 1 ing-003, 1 pwr-001 | 4 med-022 | — |
| press fever reducers | med.press | 60 | 1 med-060, 1 med-083, 2 pak-017, 1 pwr-001 | 2 med-023 | — |
| pack cold and flu sachets | med.compounder | 30 | 1 med-060, 1 med-069, 1 ing-003, 2 pak-015, 1 pwr-001 | 2 med-024 | — |
| press antacid tablets | med.press | 60 | 1 chm-012, 1 med-072, 1 med-083, 2 pak-017, 1 pwr-001 | 2 med-025 | — |
| fill probiotic capsules | med.press | 60 | 1 med-078, 2 med-084, 2 pak-017, 1 pwr-001 | 2 med-026 | — |
| press iron tablets | med.press | 60 | 1 med-073, 1 med-083, 2 pak-017, 1 pwr-001 | 2 med-027 | — |
| press bone density tablets | med.press | 60 | 1 med-072, 1 med-083, 2 pak-017, 1 pwr-001 | 2 med-028 | — |
| fill vitamin D capsules | med.press | 60 | 1 med-071, 2 med-084, 2 pak-017, 1 pwr-001 | 2 med-029 | — |
| compound multivitamin syrup | med.compounder | 45 | 1 med-071, 1 med-085, 1 pak-003, 1 pwr-001 | 1 med-030 | — |
| compound calming drops | med.compounder | 30 | 1 med-079, 1 rlx-058, 1 pak-003 | 1 med-031 | — |
| steep valerian tincture | med.extractor | 240 | 2 med-057, 1 chm-004, 1 pak-003 | 1 med-032 | — |
| seal antidote ampoules | med.compounder | 60 | 1 med-076, 1 med-087, 1 pak-019, 1 pwr-001 | 1 med-033 | — |
| seal tranquilliser ampoules | med.compounder | 60 | 1 med-062, 1 med-087, 1 pak-019, 1 pwr-001 | 1 med-034 | — |
| compound sleeping draught | med.compounder | 45 | 1 med-064, 1 med-085, 1 pak-003, 1 pwr-001 | 1 med-035 | — |
| press muscle relaxants | med.press | 60 | 1 med-062, 1 med-061, 1 med-083, 2 pak-017, 1 pwr-001 | 2 med-036 | — |
| press mood stabilisers | med.press | 60 | 1 chm-014, 1 med-083, 2 pak-017, 1 pwr-001 | 2 med-037 | — |
| press migraine tablets | med.press | 60 | 1 med-060, 1 med-070, 1 med-083, 2 pak-017, 1 pwr-001 | 2 med-038 | — |
| seal antiviral ampoules | med.compounder | 60 | 1 med-067, 1 med-087, 1 pak-019, 1 pwr-001 | 1 med-039 | — |
| seal antibiotic ampoules | med.compounder | 60 | 1 med-066, 1 med-087, 1 pak-019, 1 pwr-001 | 1 med-040 | — |
| seal immune booster shots | med.compounder | 60 | 1 med-071, 1 med-079, 1 med-087, 1 pak-019, 1 pwr-001 | 1 med-041 | — |
| compound anaesthetic gel | med.compounder | 40 | 1 med-075, 1 med-086, 1 pak-011 | 1 med-042 | — |
| press strong painkillers | med.press | 60 | 2 med-060, 1 med-062, 1 med-083, 2 pak-017, 1 pwr-001 | 2 med-043 | — |
| compound aloe burn gel | med.compounder | 30 | 1 med-080, 1 med-086, 1 pak-011 | 1 med-044 | — |
| tube fresh aloe gel | any.bench | 20 | 2 veg-069, 1 pak-011 | 1 med-044 | — |
| fill liver support capsules | med.press | 60 | 1 med-079, 1 med-074, 2 med-084, 2 pak-017, 1 pwr-001 | 2 med-045 | — |
| compound immune tonic | med.compounder | 45 | 1 med-079, 1 med-085, 1 pak-003 | 1 med-046 | — |
| compound anti-itch lotion | med.compounder | 40 | 1 med-069, 1 med-086, 1 pak-003 | 1 med-047 | — |
| press decongestants | med.press | 60 | 1 med-069, 1 med-082, 1 med-083, 2 pak-017, 1 pwr-001 | 2 med-048 | — |
| compound recovery tonic | med.compounder | 45 | 1 med-071, 1 med-073, 1 med-085, 1 pak-003, 1 pwr-001 | 1 med-053 | — |
| press cortisone tablets | med.press | 60 | 2 med-061, 1 med-083, 2 pak-017, 1 pwr-001 | 2 med-054 | — |
| compound wound salve | med.compounder | 40 | 1 med-080, 1 med-081, 1 med-086, 1 pak-011 | 1 med-055 | — |
| fill nasal spray | med.compounder | 20 | 1 med-087, 1 pak-027 | 1 med-088 | — |
| incinerate expired tablets | med.disposal | 30 | 4 med-049, 1 pwr-001 | 1 san-065 | — |
| neutralise expired liquids | med.disposal | 30 | 2 med-050, 1 chm-037, 1 pwr-001 | 1 chm-084 | — |
| crush expired ampoules | med.disposal | 20 | 2 med-051, 1 pwr-001 | 1 scr-017 | — |
| incinerate expired ointment | med.disposal | 30 | 2 med-052, 1 pwr-001 | 1 san-065 | — |
| make reactor stirrer seal | any.bench | 60 | 1 pol-052, 1 mec-006 | 1 med-089 | — |
| make extractor mesh screen | any.bench | 45 | 1 met-057 | 1 med-090 | — |
| make fermenter air filter | any.bench | 45 | 1 cer-025, 1 pol-035 | 1 med-091 | — |
| make tablet press die set | any.bench | 90 | 1 met-049, 1 mec-005 | 1 med-092 | — |
| make compounding hood filter | any.bench | 45 | 1 cer-025, 1 met-007 | 1 med-093 | — |
| make disposal burner nozzle | any.bench | 60 | 1 met-056, 1 mec-049 | 1 med-094 | — |
| build synthesis reactor kit | any.bench | 180 | 1 fur-001, 1 med-089, 1 mec-010, 2 mec-001 | 1 med-095 | — |
| build herb extractor kit | any.bench | 120 | 1 fur-001, 1 med-090, 1 mec-008, 2 mec-001 | 1 med-096 | — |
| build culture fermenter kit | any.bench | 180 | 1 fur-001, 1 med-091, 1 ecp-010, 2 mec-001 | 1 med-097 | — |
| build tablet press kit | any.bench | 120 | 1 fur-001, 1 med-092, 1 mec-043, 2 mec-001 | 1 med-098 | — |
| build compounding hood kit | any.bench | 120 | 1 fur-001, 1 med-093, 1 mec-009, 2 mec-001 | 1 med-099 | — |
| build drug disposal unit kit | any.bench | 120 | 1 fur-001, 1 med-094, 1 lgt-008, 2 mec-001 | 1 med-100 | — |

## Codex

| id | about | flavour |
|---|---|---|
| med.reactor | Synthesises active powders from chemicals: painkillers, antibiotics, antivirals, sedatives and antidotes. | PRESSURE VESSEL. DO NOT OPEN DURING REACTION. COF PHARMACEUTICAL DIVISION. |
| med.extractor | Draws active powders, tinctures and extracts out of herbs grown aboard. | Herb yield per batch is audited against farm records. Discrepancies are investigated. |
| med.fermenter | Grows antibiotic broth, vaccine antigen, vitamins and probiotics from cultures. | Sterility verified, air filter seated, rev 8. Contamination logged as zero. Logged. |
| med.press | Presses powders into tablets and fills capsules into blister packs. | Every tablet is counted at the press. Counts are reconciled against medbay issue monthly. |
| med.compounder | A clean hood for mixing syrups, ointments, drops and sterile ampoules. | Gown, glove, mask. Hood airflow is monitored. Breaches are logged against the operator. |
| med.disposal | Burns, neutralises or crushes expired medicines safely. | EXPIRED STOCK ONLY. NO RETRIEVAL AFTER LOADING. DISPOSAL IS WITNESSED. |
| med-001 | A tablet that eases pain at a slight cost in toxin, leaving an empty blister. | Two for a headache. One for a shift. None for a grievance. |
| med-002 | A tablet that treats bacterial infection and raises immunity; it upsets the gut slightly. | Complete the full course. Partial courses are recorded on Form 2A. |
| med-003 | A daily vitamin tablet that raises immunity. | Issued in lieu of sunlight. Sunlight is not provisioned. |
| med-004 | A strong tablet that eases stress heavily but leaves the operator slow and flat. | MAY CAUSE DROWSINESS. DO NOT OPERATE STATION EQUIPMENT. SHIFT CONTINUES. |
| med-005 | A pill that induces sleep and eases stress, at some cost to mood. | Sleep is a scheduled activity. The pill keeps the schedule. |
| med-006 | A tablet that eases anxiety, with slight loss of enjoyment. | Anxiety is not a recognised condition under the operating contract. Tablets are issued anyway. |
| med-007 | A capsule that treats viral illness and raises immunity, with slight toxin. | Outbreaks are reported to the Company before the operator is told. |
| med-008 | A bottled antiseptic for cleaning wounds; it stings on use. | Stinging indicates contact. Contact is the instruction. |
| med-009 | A tablet that eases swelling and pain. | Bulkhead contact injuries are self-reported. Self-reports are filed and not read. |
| med-010 | A tablet that settles nausea and helps clear toxins. | Low gravity nausea is expected in the first cycles. Productivity is also expected. |
| med-011 | A vaccine injection that builds strong immunity; it is briefly painful and keeps only a short time. | Vaccination is a condition of contract. Refusal is a condition of termination. |
| med-012 | An injection that numbs deep pain, leaving the limb weak for a time. | RESTRICTED. MEDBAY ADMINISTRATION ONLY. RECORD SITE AND TIME. |
| med-013 | Salts and sugar mixed with water to restore fluid when the body runs dry. | Mix with drinking water only. One sachet per litre. The litre is measured. |
| med-014 | Charcoal tablets that bind poisons in the gut. | Black stool is expected. It is not to be reported as a fault. |
| med-015 | A tablet against allergic reaction; it causes slight drowsiness. | Farm pollen counts are not published. Take as needed. |
| med-016 | A syrup that soothes a cough and aids rest. | Berry flavour Type 1. The flavour was not tested on operators. |
| med-017 | An ointment that cools burns and helps them heal. | Galley burns are classed as operator error. Ointment is issued without prejudice. |
| med-018 | A warming balm for sore muscles after work or exercise. | Apply after shift. Muscle strain during shift is not recognised. |
| med-019 | A cream that clears fungal skin infections. | Sealed boots, warm decks. Infection rates are within fleet norms. |
| med-020 | An ointment that keeps a small wound from infection. | Minor wounds do not require a report. Infected ones do. |
| med-021 | Drops that soothe dry, sore eyes. | Recycled air dries the eye. Air quality is within specification. |
| med-022 | A sweet lozenge that eases a sore throat. | Dissolve slowly. Sugar content counts against the daily ration. |
| med-023 | A tablet that brings down a fever and eases aches. | Report fever above 38 C on Form 23F. Then return to station. |
| med-024 | A powdered remedy for colds and flu, dissolved in hot water, that aids rest. | Respiratory illness spreads by air. The air is shared. Report symptoms. |
| med-025 | A chalky tablet that settles an acid stomach. | Galley output is nutritionally compliant. Antacids are stocked regardless. |
| med-026 | Live gut bacteria in a capsule that raise immunity; it keeps only a short time. | LIVE CULTURE. USE BEFORE DATE. DO NOT STORE NEAR HEAT. |
| med-027 | An iron supplement that supports healthy blood. | Pallor is noted at inspection. Supplements are noted alongside. |
| med-028 | Calcium tablets that slow the bone loss of low gravity. | Bone loss is a known contract condition. Fracture claims are reviewed against compliance. |
| med-029 | A vitamin capsule that supports bones and immunity in the absence of sunlight. | One capsule daily. There is no daylight to substitute. Ref 2900/D. |
| med-030 | A sweet syrup of vitamins that raises immunity. | Liquid format issued to operators who refuse tablets. Refusals are noted. |
| med-031 | Herbal drops that ease stress. | A few drops in tea. Stress readings are reviewed at end of cycle. |
| med-032 | A valerian tincture that aids sleep and slightly eases stress. | Smells of old socks. Works. Odour complaints are not accepted. |
| med-033 | An injected antidote that rapidly clears poison. | EMERGENCY USE. LOG EXPOSURE SOURCE BEFORE ADMINISTRATION IF CONSCIOUS. |
| med-034 | A powerful injected sedative that heavily calms and immobilises the recipient. | For crisis events only. Crisis events are defined in Annex T and reported upward. |
| med-035 | A strong liquid sleep aid that brings heavy rest, with slight toxin. | Take in bunk. Effects begin within minutes. Falls are not covered. |
| med-036 | A tablet that eases muscle cramp and stress, leaving the body slack. | Reduces muscle tone. Do not take before lifting duties. Lifting duties are daily. |
| med-037 | A tablet that steadies mood over time, with slight toxin. | Daily dose. Missed doses are recorded by the dispenser. The dispenser remembers. |
| med-038 | A tablet against migraine pain that makes rest harder. | Dim station lighting during attack. Lighting hours are still billed. |
| med-039 | An injected antiviral, stronger than the antiviral capsule. | Second line. Issue requires a failed first line on record. |
| med-040 | An injected antibiotic for serious infection. | RESERVE STOCK. MEDBAY AUTHORISATION REQUIRED. FORM 40A. |
| med-041 | An injection that raises immunity ahead of an outbreak. | Administered fleet-wide on notice. Notice is short. |
| med-042 | A numbing gel for local pain. | Numbs on contact. Wash hands before touching eyes. Learned the hard way. |
| med-043 | A strong painkiller that dulls body and mind, at a real cost in toxin. | CONTROLLED. COUNT ON ISSUE. COUNT ON RETURN. DISCREPANCIES REPORTED. |
| med-044 | An aloe gel that soothes minor burns; it keeps only a short time. | Grown aboard, squeezed aboard, applied aboard. Billed aboard. |
| med-045 | A capsule that helps the body clear toxins. | Brew consumption is a private matter. Liver function is a Company matter. |
| med-046 | A herbal tonic that raises immunity. | Efficacy unverified. Stocked as a morale measure. Morale unverified. |
| med-047 | A lotion that calms itching skin. | Scratching through issued garments damages the garment. Apply lotion. |
| med-048 | A tablet that clears a blocked nose, at some cost to calm and sleep. | Clears the airway. Keeps the operator awake. Both are useful to the Company. |
| med-049 | Tablets and capsules past their date, burned in the drug disposal unit. | EXPIRED. DO NOT ISSUE. DO NOT CONSUME. DISPOSAL UNIT ONLY. |
| med-050 | Liquid medicine past its date, neutralised in the drug disposal unit. | Expired liquids are not to be poured into grey water. Proc 212. |
| med-051 | An ampoule past its date, crushed in the drug disposal unit. | Glass for the crusher. Never for a vein. Disposal is witnessed. |
| med-052 | Ointment past its date, burned in the drug disposal unit. | Separation and odour indicate expiry. So does the date. |
| med-053 | A tonic that speeds recovery after illness or injury. | Issued on return to duty. Return to duty is not optional. |
| med-054 | A steroid tablet that eases pain and swelling but lowers immunity. | Short courses only. Long courses require medbay review on Form 54C. |
| med-055 | A salve that helps wounds heal faster. | Faster healing returns operators to station sooner. Hence its issue. |
| med-056 | Bark pruned from willow grown aboard; the source of salicylate. | Pruning is scheduled. Unscheduled pruning is counted as harvest theft. |
| med-057 | Root lifted from valerian pots for sedatives and sleep tincture; it dries out quickly. | Process within ten days. Strong odour is normal and not a spoilage indicator. |
| med-058 | Flowers cut from echinacea and tinctured for immune remedies; they wilt quickly. | Cut at full bloom. Steep the same shift. Wilted stock is written off. |
| med-059 | Salicylate powder from willow bark or the reactor, made into painkillers and balms. | Batch assay attached. Purity Grade B. Grade A is not produced aboard. |
| med-060 | Active painkiller powder, pressed into tablets and packed into sachets. | ACTIVE INGREDIENT. LABEL AND LOCK. INVENTORY BY WEIGHT. |
| med-061 | Anti-inflammatory powder for tablets and cortisone. | Store dry. Clumped powder is reclassified as waste and charged to the station. |
| med-062 | Sedative powder for calming tablets, ampoules and relaxants. | Handle under hood only. Inhalation causes sleep. Sleep on shift is a finding. |
| med-063 | Anxiolytic powder for tablets that ease anxiety. | Controlled substance. Weighed in, weighed out. SN 0063 2271. |
| med-064 | Sleep-inducing powder for sleeping pills and draughts. | DO NOT INHALE. DO NOT HANDLE WITHOUT MASK. HOOD ONLY. |
| med-065 | A mould culture broth grown on spoiled food, purified into antibiotics; it spoils fast. | Grown on spoiled food. Classified as pharmaceutical feedstock from that moment. |
| med-066 | Purified antibiotic powder for tablets, ointments and ampoules. | Purity tested, passed, rev 2. Batch held one cycle pending a second signature. |
| med-067 | Antiviral powder for capsules and ampoules. | High-cost synthesis. Wastage is charged at full reagent cost. |
| med-068 | A live antigen culture for vaccines that must be sealed into ampoules soon. | FRAGILE CULTURE. SEAL WITHIN FIVE DAYS. DO NOT FREEZE AND THAW. |
| med-069 | Antihistamine powder for tablets, drops, sachets and lotions. | Multi-use stock. Allocation between products is set by medbay, not the operator. |
| med-070 | Antiemetic powder from mint or the reactor. | Mint-derived batches are logged separately for yield comparison. |
| med-071 | Concentrated vitamins from algae or yeast. | Farm output, concentrated. Credited to the pharmaceutical account, not the farm's. |
| med-072 | Calcium powder for bone density and antacid tablets. | Ground eggshell, sieved to 100 micron. Nothing aboard is wasted twice. |
| med-073 | Iron powder for blood supplements and recovery tonic. | Reacted from scrap iron. Pharmaceutical grade on assay. Assay attached. |
| med-074 | Activated charcoal powder that binds poisons. | Medicinal grade. Do not substitute filter charcoal. Proc 74. |
| med-075 | Anaesthetic powder for nerve blocks and numbing gel. | RESTRICTED. MEDBAY USE ONLY. SIGN FOR EACH GRAM. |
| med-076 | Antidote powder for sealing into emergency ampoules. | Held for incidents. Stock level is checked weekly. Incidents are not scheduled. |
| med-077 | Antifungal powder for antifungal creams. | Demand tracks deck humidity. Deck humidity is within specification. |
| med-078 | Live probiotic powder for capsules; it keeps only a short time. | Freeze-dried live culture. Viability declines on the shelf and on the record. |
| med-079 | A herbal tincture base for drops, tonics, capsules and booster shots. | Alcohol base. Not for consumption as a beverage. It has been tried. |
| med-080 | Aloe extract for burn gel and wound salve; it keeps only a short time. | Extracted from station-grown aloe. Leaf count audited. |
| med-081 | Concentrated antiseptic for bottling and ointments. | CONCENTRATE. DILUTE BEFORE USE. NEVER APPLY UNDILUTED. |
| med-082 | Cough-suppressing powder for syrups, lozenges and decongestants. | Menthol-derived batches noted on Form 82M. Strong vapour. Use hood. |
| med-083 | A starch binder that holds tablets together. | Binder ratio per formulation sheet. Crumbling tablets indicate operator variance. |
| med-084 | An empty capsule shell to be filled with powder. | Size 0. Only one size is cast aboard. Doses are adjusted to fit. |
| med-085 | A sugar syrup base for liquid medicines. | Sugar for syrup is drawn from galley stock. The galley has been informed. |
| med-086 | A wax or silicone base for ointments, gels and salves. | Inert base. Shelf stable. The only stable thing in medbay. |
| med-087 | Sterile saline for ampoules, eye drops and nasal spray. | STERILE UNTIL OPENED. SINGLE USE. DISCARD REMAINDER. |
| med-088 | A saline nasal spray that clears the nose and slightly raises immunity. | One spray per side. Bottle is returned for washing, not kept. |
| med-089 | A replacement stirrer seal fitted to the synthesis reactor; it wears into broken parts. | Seal weeping at shaft. Within limit. Barely. Tag 0089. |
| med-090 | A replacement mesh screen fitted to the herb extractor; it wears into metal scrap. | Mesh 200. Torn mesh passes plant matter into product. Inspect each batch. |
| med-091 | A replacement air filter fitted to the culture fermenter; it wears into broken parts. | Filter integrity tested, rev 3. Pressure drop rising. Next test overdue. |
| med-092 | A replacement die set fitted to the tablet press; it wears into metal scrap. | Die face stamped COF. Every tablet aboard carries the mark. |
| med-093 | A replacement filter fitted to the compounding hood; it wears into broken parts. | Hood filter replaced on schedule. Schedule set by procurement, not by load. |
| med-094 | A replacement burner nozzle fitted to the drug disposal unit; it wears into metal scrap. | Burn temperature verified at 850 C. Verification log signed. Signature illegible. |
| med-095 | A crated kit that installs a synthesis reactor. | PRESSURE VESSEL INSIDE. INSTALL PER MANUAL. MANUAL ON BACK ORDER. |
| med-096 | A crated kit that installs a herb extractor. | Herb processing on station does not alter medical issue entitlement. |
| med-097 | A crated kit that installs a culture fermenter. | Commissioning requires a sterility run. The sterility run requires the fermenter. |
| med-098 | A crated kit that installs a tablet press. | Station tablet production is subject to quarterly reconciliation, Form 98R. |
| med-099 | A crated kit that installs a compounding hood. | Clean room classification applies once installed. Classification is not a guarantee. |
| med-100 | A crated kit that installs a drug disposal unit. | Disposal capacity reduces medical stock losses. Losses are still charged. |
