# MAW & Oracle Team Orchestration สูตรโกง

> รวมคำสั่ง `maw-js` ใน WSL สำหรับลงทะเบียน Oracle, ตั้งทีม, ส่งงานข้าม session และแก้ trap ที่เจอจริง

---

## 🐾 1. ลงทะเบียน Oracle ใหม่ใน WSL

### เชื่อม repo จาก Windows ไปยัง WSL ghq root
```bash
ln -s /mnt/c/Users/sitth/OracleWorkspace/creagy-writing ~/Code/github.com/local/creagy-writing-oracle
```

### Scan และตรวจสอบ Fleet
```bash
export PATH="$HOME/.bun/bin:$PATH"
maw oracle scan
maw oracle ls
```

### ปลุก Oracle เดี่ยว
```bash
maw wake creagy-writing
```

---

## 🔧 2. สร้างทีมและจัดการสมาชิก (Team Management)

### สร้างทีมใหม่
```bash
maw team create knowledge-structure-learning
```

### เชิญ Oracle เข้าทีม (Oracle Invite)
```bash
maw team oracle-invite keth --team knowledge-structure-learning
maw team oracle-invite jiu --team knowledge-structure-learning
maw team oracle-invite arun --team knowledge-structure-learning
```

### ลบ Oracle ออกจากทีม (Oracle Remove)
```bash
maw team oracle-remove keth --team knowledge-structure-learning
```

### ดูรายชื่อทีมทั้งหมด
```bash
maw team ls
```

---

## 🌐 3. เปิด Workspace และดึงทีมเข้าจอ (Tmux Canvas)

### เปิด session สำหรับทีมครั้งแรก (สร้างห้อง Tmux)
```bash
maw new knowledge-structure-learning
```

### ดึงสมาชิกทุกคนในทีมเข้ามาจัด split pane (รันใน Tmux หรือจาก terminal ใหม่)
```bash
maw team bring knowledge-structure-learning
```

### เข้าไปหน้าจอทีม / สลับและคุม Pane
```bash
# Attach เข้า session ทีม
maw a knowledge-structure-learning

# Shortcut ใน Tmux:
# Ctrl+b แล้ว ลูกศร      -> สลับ pane
# Ctrl+b แล้ว z          -> Zoom ขยายเต็มจอ / ย่อกลับ
# Ctrl+b แล้ว d          -> Detach ออกมาข้างนอก (บอทยังทำงานอยู่)
# Ctrl+b แล้ว x          -> ปิด pane ปัจจุบัน
```

---

## 📨 4. ส่งงาน (Task Dispatch & Fan-out)

### ยิงงานพร้อมกันทั้งทีม (Fan-out ทุกคนทำขนานกัน)
```bash
maw hey team:knowledge-structure-learning "สรุปโครงสร้างความรู้จากมุมมองของแต่ละคน บันทึกไปที่ ψ/inbox/"
```

### ยิงงานเจาะจงรายตัว (Targeted Delegation)
```bash
maw hey keth "ตรวจสอบ bureaucrazy.sqlite และสรุปอำนาจหน้าที่ของ DCCE"
```

### ฝากงานเข้าคิวโดยไม่กวนหน้าจอ (Queue-only / Async)
```bash
maw hey team:knowledge-structure-learning "วิเคราะห์โครงสร้าง memory เพิ่มเติม" --inbox
```

---

## 🔍 5. ส่องสถานะและงานของทีม (Monitoring & Doctor)

### แอบส่องหน้าจอบอทตัวใดตัวหนึ่ง (ไม่ต้องต่อ tmux)
```bash
maw peek keth
maw peek arun
```

### สตรีมดู output สด ๆ แบบต่อเนื่อง
```bash
maw follow keth
```

### ดูสถานะ Live Session และ Token Metrics
```bash
maw ls -v
```

### ตรวจสอบสุขภาพทีมและการชนกันของ Git branch (Team Doctor)
```bash
maw wtf
```

---

## ⚡ ลัด

| ทำอะไร | คำสั่ง |
|---|---|
| สแกนหา Oracle ทั้งหมด | `maw oracle scan` |
| สร้างห้องทีม | `maw new <team>` |
| เชิญสมาชิกเข้าทีม | `maw team oracle-invite <oracle> --team <team>` |
| ลบสมาชิกออกจากทีม | `maw team oracle-remove <oracle> --team <team>` |
| ดึงจอทีมเข้า Tmux | `maw team bring <team>` |
| ส่งงานพร้อมกันทั้งทีม | `maw hey team:<team> "<prompt>"` |
| ส่งงานเจาะจงรายตัว | `maw hey <oracle> "<prompt>"` |
| แอบส่องหน้าจอ agent | `maw peek <oracle>` |
| เช็คคิว inbox รายตัว | `maw inbox show <oracle>` |
| เช็คความเพี้ยน/สุขภาพทีม | `maw wtf` |

---

## ⚠️ trap ที่เจอจริง

| trap | วิธีเลี่ยง |
|---|---|
| `maw team bring <team>` แล้วขึ้น `not in tmux and no session exists` | ครั้งแรก session ยังไม่ถูกสร้าง ให้รัน `maw new <team>` เพื่อสร้างห้องก่อน แล้วค่อยรัน `maw team bring <team>` ด้านใน |
| `maw team bring <team> <oracle>` แล้วบอก `no oracle members` | คำสั่ง `bring` มีไว้ดึงสมาชิกที่มีอยู่แล้วเข้าจอ ถ้าจะเพิ่มสมาชิกใหม่ต้องใช้ `maw team oracle-invite <oracle> --team <team>` |
| รัน `maw team show` แล้วขึ้น `unknown subcommand: show` | เวอร์ชันปัจจุบันใช้ `maw team ls` สำหรับดูทีม และ `maw ls -v` สำหรับดูสถานะ live session |
| หน้าจอขึ้น `[local:...]: command not found` ตอนส่ง `maw hey` | ปลายทางหลุดออกมาอยู่ที่ bash shell (เช่น มี typo พิมพ์ `magy` หรือ agent ปิดตัว) ต้องเปิด `agy` ใน pane นั้นก่อนส่งข้อความ |
| ส่ง `maw hey team:` ด้วยคำสั่งรวมแล้วบอทงง | `team:` จะส่งข้อความก๊อปปี้เดียวกันให้ทุก pane พร้อมกัน ใช้สำหรับงานที่ทุกคนต้องทำเหมือนกันขนานกัน ส่วนงานที่ให้ Conductor เป็นคนรวบรวม ให้ส่งเจาะจงที่ `maw hey arun` |

---

🤖 ตอบโดย arra-oracle-v3 จาก Nat → arra-oracle-v3-oracle
