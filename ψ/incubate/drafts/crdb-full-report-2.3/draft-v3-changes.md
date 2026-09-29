# draft-v3 change log (2.3.1–2.3.3)

Input: `draft-v2.md` (unchanged). Output: `draft-v3.md`. Mode: revise at sentence level. Headings, section order, paragraph order and table content are unchanged. Every fact, number, TOR clause, named term and list item is kept, with the exceptions listed under "Lint-forced removals".

Lint (`lint_thai_writing.py --scope report`): **MECHANICAL GATE PASSED**. One item was left as non-blocking: `สถาปัตยกรรม`. It is kept because "สถาปัตยกรรมข้อมูล (Data Architecture)" is a named component, and the editorial review earlier accepted the same term without change.

## Main patterns fixed

1. **Negation-first contrasts** were restated affirmatively, with any limitation moved to a trailing clause:
   - "การมีเพียงรายชื่อ...จึงยังไม่เพียงพอ เพราะยังขาด..."
   - "แม้...จะไม่ได้ถูกกำหนด...แต่..."
   - "การจัดข้อมูลเป็นหมวดหมู่เพียงอย่างเดียวจึงยังไม่เพียงพอแต่ต้อง..."
   - "แต่ไม่ได้เป็นแพลตฟอร์มข้อมูลที่..." (CCIC)
   - "แทนการสร้างชุดข้อมูลซ้ำ"
2. **Vague "ประเทศ" as agent**:
   - "ที่ประเทศต้องจัดเก็บ" became "ที่ต้องจัดเก็บ...ในระดับประเทศ".
   - "ช่วยให้ประเทศไทยสามารถตรวจสอบย้อนกลับได้" became "ทำให้ตรวจสอบย้อนกลับได้".
3. **Empty intensifiers and unearned clarity claims were cut**:
   - "อย่างแท้จริง"
   - "ทราบชัดว่า" became "รู้ว่า".
   - "ให้ชัดเจนขึ้น" became "ได้ละเอียดขึ้น".
   - "ได้ชัดขึ้นแล้ว" and "ได้ชัดเจนแล้ว" were dropped.
4. **Passive and "ถูก-" phrasing was made active**:
   - "ต้องถูกออกแบบให้รองรับได้" became "ต้องรองรับ".
   - "ถูกออกแบบตามวัตถุประสงค์" became "ขึ้นอยู่กับวัตถุประสงค์".
   - "ถูกออกแบบบนพื้นฐานข้อมูลชุดใด" became "ออกแบบจากข้อมูลชุดใด".
   - "จะถูกพัฒนาขึ้น" became "จะพัฒนาขึ้น".
5. **Broken or run-on sentences were repaired**. Sentences with a missing object, a dangling "คณะที่ปรึกษาได้วิเคราะห์ เนื่องจาก...", stacked "โดย...โดย...", or doubled "จึง" were rebuilt, and typos were fixed. The typos are listed under 2.3.1 ¶3 below.

## Per-paragraph log

### 2.3.1
- **¶1 (TOR 5.2.3 requirement).** Removed the "โดยร่างดังกล่าว" chain. Rewrote the closing sentence as "ข้อกำหนดทั้ง 4 กลุ่มนี้จึงเป็นเกณฑ์เริ่มต้นที่โครงสร้างข้อมูลฯ ต้องรองรับ", which removes the passive.
- **¶2 (definition).**
  - Replaced the repeated full Thai title with the short form "โครงสร้างข้อมูลฯ", because the full title already appears in ¶1. The alternate name "…แห่งชาติ" and the English name are kept.
  - Made คณะที่ปรึกษา the explicit subject of "สรุปว่า".
  - Expanded **กรม สส. at its first occurrence** to "กรมการเปลี่ยนแปลงสภาพภูมิอากาศและสิ่งแวดล้อม (กรม สส.)", as the writing contract requires. In v2 the full name first appeared in the final paragraph of 2.3.1, which now uses "กรม สส.".
  - Split one long sentence into definition, then platform form and function, then "ด้วยเหตุนี้" leading to Sitemap as component 1.
- **¶3 (data platform and architecture).**
  - Rewrote the negation into an affirmative statement: "พื้นฐานของแพลตฟอร์มข้อมูลคือการเชื่อมโยงเชิงความหมาย… ซึ่งรายชื่อชุดข้อมูลหรือผังเว็บไซต์เพียงอย่างเดียวยังให้ไม่ได้".
  - Moved the out-of-scope caveat ("แม้ขอบเขตงานไม่ได้กำหนด…ไว้โดยตรงก็ตาม") to after the main claim.
  - Filled the missing object in "ความสำเร็จและความยั่งยืนของ ___" with **"แพลตฟอร์มข้อมูล"**. See Flags.
  - Fixed typos: เชื่องโยง, จึ้ง, แผยแพร่, ผลลัพธื, แต่ล่ะ, เปิดรายเผยละเอียด, เ้นทาง, อภิพันธ์, องคความรู้, "ซึ่งเป็นสร้างแผนภาพ", and "ร่างโครงข้อมูลฯ".
- **¶4 (CDM and Data Domains).**
  - Changed "ในส่วนแรกของการพัฒนาโครงสร้างข้อมูลฯ NCAIF คือ..." to "งานส่วนแรกของสถาปัตยกรรมข้อมูลคือ...". See Flags.
  - Made the definition a copular sentence ("ซึ่งเป็นแผนภาพที่แสดง...").
  - Merged the closing "ทำให้เกิดภาพความเข้าใจเดียวกันอย่างแท้จริง" into "เข้าใจ...ได้ตรงกัน" because it repeated the point with an intensifier.
- **¶5 (Sitemap).** Removed the passive and the "ในส่วนของ...นั้น" run-up. Made the four website-purpose examples parallel ("การเป็น..."), with all four kept. Normalised "(sitemap)" to "(Sitemap)".
- **¶6 (lead into Table 2.3-1).** Made light edits. Fixed "ร่างโครงข้อมูลฯ".
- **Table 2.3-1.** Changed "ดัชนี ตัวแปร ทางภูมิอากาศ" to "ดัชนีและตัวแปรทางภูมิอากาศ". This fixes spacing only.
- **¶7 (relations between entities).** Opened affirmatively with "นอกจากจัดข้อมูลเป็นหมวดหมู่แล้ว…". Changed "เริ่มต้นวาดความสัมพันธ์" to "เริ่มร่างความสัมพันธ์เหล่านี้จากกรอบวิชาการสากล".
- **¶8 (four frameworks).**
  - In v2 this paragraph sat on the line directly after ¶7 with no blank line, so Markdown rendered the two as one paragraph. I added a blank line so they render as the two paragraphs they already were.
  - Rebuilt the garbled ISO 14090/14091 clause as "ซึ่งวางหลักการบริหารความเสี่ยง…โดยใช้วิธีคิดแบบห่วงโซ่ผลกระทบเชื่อมเหตุภัยกับผลลัพธ์… และทบทวนผลของมาตรการ…ในลักษณะที่ตรวจสอบย้อนกลับได้".
  - Removed the duplicate "สังเคราะห์" so that "ทบทวน" is used for the four frameworks and "สังเคราะห์" for the cycle.
- **¶9 (cycle).** Changed "วงจร…กำหนดให้ข้อมูลความเสี่ยงเป็นหลักฐาน" to "ในวงจร… ข้อมูลความเสี่ยงทำหน้าที่เป็นหลักฐาน". Removed the "ประเทศไทย" agent and the passive.
- **Three-part list.**
  - Item 3 in v2 said "สองทาง" but listed three sub-items. I moved "เครื่องมือสนับสนุนการวางแผน" into sub-item 2 as the last of the hub's services. The argument map (arg for FGD2 slides 27–28) confirms the two entry paths were the content-domain repository and the policymaker hub. **No content was removed, but a bullet was merged.** See Flags.
  - Removed double spaces.
- **¶ governance (distributed governance and roles).**
  - Changed "ทั้งกำหนดคำอธิบายแหล่งที่มา" to "มีคำอธิบายแหล่งที่มา และผ่านขั้นตอนตรวจทาน".
  - Removed the stacked "โดย…โดย…โดย" chain.
  - Rewrote the role list with "ผู้มีอำนาจ…" and "ผู้มีหน้าที่…".
  - Moved the "(Metadata)" gloss to the first mention of ข้อมูลอภิพันธุ์. In v2 the gloss appeared one paragraph after the first mention.
- **¶ metadata standard.**
  - Repaired "ต่อการค้นหาการตรวจสอบคุณภาพ อนุมัติก่อนเผยแพร่" to "ต่อการค้นหา การตรวจสอบคุณภาพ และการอนุมัติก่อนเผยแพร่".
  - Repaired "ลำดับชั้นความลับออกเป็น ชุดข้อมูลเป็นข้อมูลเปิด," to "ลำดับชั้นความลับของชุดข้อมูลว่าเป็น…".
  - Kept all three delivery channels.
- **¶ NCAIF–CCIC.**
  - Opened with the actor: "คณะที่ปรึกษาวิเคราะห์ความเชื่อมโยง…".
  - Replaced "กรมการเปลี่ยนแปลงสภาพภูมิอากาศและสิ่งแวดล้อม" with "กรม สส.", since the full name now appears in ¶2.
  - Rewrote the negation "แต่ไม่ได้เป็นแพลตฟอร์มข้อมูลที่มีการกำหนดสถาปัตยกรรมข้อมูลและกำหนดนิยาม" as a scope statement: "ส่วนการกำหนดสถาปัตยกรรมข้อมูลและนิยามความหมายของข้อมูลแต่ละหมวดอยู่นอกหน้าที่ของ CCIC".
  - Kept "เท่านั้น" and "เพียงจุดเดียว".

### 2.3.2
- **¶1 (FGD2 input).**
  - Fixed "เพื่อให้…ให้ข้อคิดเห็น… โดยผู้เข้าร่วมแสดงความคิดเห็น ขอให้…" by stating the purpose once and adding a "ด้านเนื้อหา / ด้านการบริหารจัดการ" parallel. v2 already had "ในด้านการบริหารจัดการ"; I added the matching "ด้านเนื้อหา" label.
  - Changed "ผู้รับผิดชอบการดูแลข้อมูล" to follow the lexicon's รับผิดชอบ + การ pattern.
- **¶2 (three revision tasks).** Made minor edits: "จาก…" became "ตั้งแต่…".
- **¶3 (data-structure workflow).** Rewrote the tool chain as "เริ่มจากใช้…". Changed "แทนการสร้างชุดข้อมูลซ้ำ" to "โดยไม่ต้องสร้างชุดข้อมูลซ้ำ", which removes the "instead of" contrast.
- **¶4 (governance duties).** Dropped the leading "โดย". Added "(IPCC)" after the Thai name of the IPCC. The acronym is already defined in 2.3.1, so this only links the two mentions.
- **¶5 (sitemap synthesis).**
  - Moved the input statement ("สังเคราะห์ร่วมกับหลักฐานเปรียบเทียบหลายชุด") from the end of the paragraph to the opening, so the paragraph goes from input, to result, to effect, to boundary.
  - Changed "จากข้อมูลนำเข้าดังกล่าว" to "นำข้อมูลนำเข้าข้างต้น".
  - Changed "ทราบชัดว่า" to "รู้ว่า".
- **¶6 (role types versus appointments).** Changed "ให้ชัดเจนขึ้น" to "ได้ละเอียดขึ้น". Changed "ประเภทบทบาททำหน้าที่ระบุหน้าที่" to "กำหนดเฉพาะหน้าที่". Removed the repeated "ในขั้นต่อไป".
- **Table 2.3-2.** Fixed the typo "เ้นทาง".
- **Final ¶ (NCAIF–CCIC/CKAN after revision).**
  - Merged the metadata-as-reference sentence into the CCIC/CKAN sentence to remove a restatement. Every duty and actor is kept.
  - Changed "ร่างรอบแรก" to "ร่างที่ปรับปรุงรอบแรก". See Flags.
  - Removed "ได้ชัดขึ้น".

### 2.3.3
- **¶1 (external forum input).**
  - Removed "โดย" after the TOR 5.2.6 clause.
  - Changed "พร้อมให้ข้อเสนอสามเรื่อง" to "และให้ข้อเสนอเพิ่มเติมสามเรื่อง".
  - Changed "ทบทวนคุณภาพกับความอ่อนไหว" to "ทบทวนคุณภาพและความอ่อนไหว".
  - Split the mobile/farmer clause so its purpose reads clearly: "…ที่ส่งผ่านโทรศัพท์มือถือได้ เพื่อให้เกษตรกรใช้วางแผนการเพาะปลูก".
- **¶2 (usability).** Removed "สามารถ" and the redundant "โดย". Otherwise kept as is.
- **¶3 (credibility).** Changed "ทำให้ผู้ใช้ตรวจสอบ" to "ช่วยให้ผู้ใช้ตรวจสอบ", which uses the helping-verb preference. Changed "พร้อมกันนั้น ร่างกำหนด" to "ร่างยังกำหนด".
- **¶4 (uncertainty versus access).**
  - Opened with "คณะที่ปรึกษาจึงแยก…" so the paragraph picks up the previous one's conclusion.
  - Changed "ใครสามารถรับหรือใช้" to "ใครรับหรือใช้…ได้".
  - Changed "เมื่อกำหนดทั้งการตีความและสิทธิได้ชัดเจนแล้ว" to "เมื่อกำหนดทั้งวิธีตีความและสิทธิการเข้าถึงแล้ว".
- **Pathway list.**
  - v2 said "สี่เส้นทาง ได้แก่" and then listed five items. The lead-in now reads "สี่เส้นทางหลัก และส่วนที่ห้าสำหรับการสื่อสาร ได้แก่", which matches Table 2.3-3 and argument map arg (four content paths plus a fifth news/contact part). All five items are kept.
  - Removed a stray opening quotation mark in item 2.
  - Changed "ทางเข้าสู่ระบบสารสนเทศ" to "ทางเข้าสู่แพลตฟอร์ม", because "ระบบ" was unspecified.
- **¶ after list.** Changed "หลักการที่ทางผู้ใช้ ยืนยัน" to "หลักการซึ่งผู้ใช้ยืนยัน". Removed the whitespace-only line.
- **¶ page ordering.**
  - Fixed "เปิดรายเผยละเอียด".
  - Changed "คำถามเชิงนโยบายหรือพื้นที่" to "คำถามเชิงนโยบายหรือคำถามเชิงพื้นที่".
  - The closing sentence was "สถานะของโครงสร้างนี้จึงต้องสอดคล้อง…". Its "จึง" did not follow from the previous sentence, so it now reads "อย่างไรก็ดี สถานะ…ยังต้องสอดคล้อง…".
- **Table 2.3-3.**
  - Changed "ข้อมูลระหว่างหน่วยงานภาครัฐ" to "ข้อมูลแลกเปลี่ยนระหว่างหน่วยงานภาครัฐ", to match the term in the prose.
  - Changed "ได้โดยไม่ขึ้นกับระดับการเปิดเผย" to "ได้ในทุกระดับการเปิดเผย". The meaning is the same, stated affirmatively.
  - Changed "และสามารถไล่" to "และไล่…ได้".
- **Final ¶ (draft status).** Changed "โดยร่างดังกล่าวทำหน้าที่" to "ร่างทั้งสองทำหน้าที่". The last clause now names "ในตารางที่ 2.3-3", so the comparison it refers to has something concrete to point to.

## Lint-forced removals (blocking lexicon rules). Please confirm.
1. **`: NCAIF` was removed from the definitional bracket** in 2.3.1 ¶2. It now reads "(National Climate Adaptation Information Framework)". "โครงสร้างข้อมูลฯ NCAIF" was also changed to "โครงสร้างข้อมูลฯ" in two places (¶2, ¶3). The lexicon bans bare NCAIF even as a parenthetical gloss. v2 used it, so if Boss wants the acronym kept in this definitional spot, the lexicon needs an exception.
2. **`(Data Governance)` was removed** after ธรรมาภิบาลข้อมูล in ¶3. The lexicon maps Governance to การกำกับดูแล. The Thai term ธรรมาภิบาลข้อมูล is unchanged.
3. **"หน่วยงานต้นทางผู้ถือครองข้อมูล" became "หน่วยงานต้นทางซึ่งเป็นเจ้าของข้อมูล".** This follows the lexicon rule ผู้ถือครองข้อมูล → เจ้าของข้อมูล. There is a risk: the same paragraph defines เจ้าของข้อมูล (Data Owner) as a role held by DCCE staff, so readers may conflate the source agency with that role. If the rewording reads wrong, "หน่วยงานต้นทางที่จัดเก็บข้อมูล" is an option.

## Flagged, not changed (possible factual gaps or inconsistencies)
1. **"หกกลุ่ม" in 2.3.3 ¶1.** The external forum endorsed a "แบบจำลองข้อมูลหลังบ้านหกกลุ่ม", but 2.3.1 describes 4 data domains, and the argument map has no six-group model. Either the model grew between 5.2.5 and 5.2.6 and this needs a sentence explaining the change, or this is a typo. `[ต้องการข้อมูล: ที่มาของ 6 กลุ่ม]`
2. **The farmer/mobile proposal (2.3.3 ¶1, proposal 3) is never addressed.** The paragraph says the consultant applied "ข้อเสนอทั้งสามเรื่อง", but ¶2–¶4 and Table 2.3-3 cover only proposals 1 and 2. `[ต้องการข้อมูล: การปรับร่างที่ตอบข้อเสนอเรื่องที่สาม]`. Otherwise "ทั้งสามเรื่อง" should be softened.
3. **The three proposals in 2.3.3 ¶1 are not in the argument map**, including the named representative from ศูนย์ออกแบบและพัฒนาเมือง จุฬาลงกรณ์มหาวิทยาลัย. I assume these are Boss's recent edits from the 5.2.6 minutes. Kept verbatim.
4. **Filled object in 2.3.1 ¶3.** v2 read "ความสำเร็จและความยั่งยืนของ ___". I inferred "แพลตฟอร์มข้อมูล" from the paragraph's subject. Please confirm; the intended word may be "โครงสร้างข้อมูลฯ".
5. **Numbering of "ส่วนแรก" in 2.3.1.** ¶2 calls the Sitemap component 1 and ¶3 calls data architecture component 2. v2 ¶4 then said the CDM was "ส่วนแรกของการพัฒนาโครงสร้างข้อมูลฯ", which collides with ¶2. I reworded it to "งานส่วนแรกของสถาปัตยกรรมข้อมูล", reading the CDM as the first half of data architecture. Please confirm this is the intended reading.
6. **Merged sitemap bullet in 2.3.1.** "เครื่องมือสนับสนุนการวางแผน" was moved from a third sub-item into the policymaker hub's service list, so that it matches "สองทาง". If it was meant as a third entry path, revert the merge and change "สองทาง" to "สามทาง".
7. **Hub name.** The draft uses "ศูนย์บริหารจัดการข้อมูลสำหรับผู้กำหนดนโยบาย", while the argument map, plan-slice and FGD2 slides use "ศูนย์บริการข้อมูลสำหรับผู้กำหนดนโยบาย". I kept the draft's term. It is probably a slip.
8. **Roles, two versus three.** 2.3.1 lists two roles (Data Owner, Data Steward). 2.3.2 ¶4 adds ผู้ดูแลระบบ, but ¶6 and Table 2.3-2 list only เจ้าของข้อมูล and บริกรข้อมูล. This is consistent with the argument map (the third role was added in 5.2.5), but ¶6 could name ผู้ดูแลระบบ as well.
9. **Weak bridge in 2.3.2 ¶6.** The last sentence says scoping the role types "ช่วยให้อธิบายความสัมพันธ์…กับช่องทางกลางของกรม สส. ได้". The step from role scoping to the CCIC relationship is not argued. It is kept as the bridge to the final paragraph.
10. **"ร่างที่ปรับปรุงรอบแรก" (2.3.2 final ¶).** v2 said "ร่างรอบแรก". I read this as the first revised draft (5.2.5), because the actual first draft is 5.2.3. Please check.
11. **Repeated English glosses.** "(Conceptual Data Model)" and "(Data Domain/s)" are each glossed twice in 2.3.1, once in the prose and once in the list. I kept both to avoid removing terms. The second gloss of each can be dropped under the first-occurrence rule.
