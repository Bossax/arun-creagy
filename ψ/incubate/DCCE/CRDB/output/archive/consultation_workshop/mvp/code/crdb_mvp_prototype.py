import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

# Page config
st.set_page_config(page_title="ต้นแบบระบบ NCAIF (MVP)", layout="wide")

# Custom CSS for cards and styling
st.markdown("""
    <style>
    .stMetric { background-color: #f0f2f6; padding: 10px; border-radius: 10px; }
    .card {
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #e6e9ef;
        margin-bottom: 10px;
        background-color: white;
    }
    .thai-font { font-family: 'Sarabun', sans-serif; }
    .context-box {
        background-color: #f8f9fa;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #007bff;
        margin-bottom: 20px;
    }
    .block-container {
        max-width: 70% !important;
        padding-top: 2rem !important;
    }
    .status-green { background-color: #d4edda; color: #155724; padding: 10px; border-radius: 5px; border-left: 5px solid #28a745; margin-bottom: 10px; }
    .status-amber { background-color: #fff3cd; color: #856404; padding: 10px; border-radius: 5px; border-left: 5px solid #ffc107; margin-bottom: 10px; }
    .status-red { background-color: #f8d7da; color: #721c24; padding: 10px; border-radius: 5px; border-left: 5px solid #dc3545; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- Sidebar ---
st.sidebar.title("ต้นแบบระบบ NCAIF")
st.sidebar.write("Workshop Anchor Artifacts (v5)")

# Translated MVP Labels
mvp_labels = {
    "MVP-1": "บริการสรุปนโยบาย (Policy Briefing)",
    "MVP-2": "สถิติภัยพิบัติภูมิอากาศ (Disaster Stats)",
    "MVP-3": "คลังข้อมูลความเสี่ยง (Data Inventory)",
    "MVP-4": "คู่มือการตีความ (Uncertainty Guide)"
}

mvp_selection = st.sidebar.radio(
    "เลือก MVP ที่ต้องการทดสอบ",
    list(mvp_labels.values())
)

st.sidebar.markdown("---")
st.sidebar.info("ต้นแบบนี้ใช้แสดงความแตกต่างของ **มูลค่าการสนับสนุนการตัดสินใจ** ระหว่างระดับปฏิบัติ (L1) และระดับอุดมคติ (L2)")

# --- Helper Components ---
def level_toggle():
    return st.toggle("สลับไปยังระดับอุดมคติ (Level 2 - Ideal)", value=False)

def decision_label_component(level):
    if level == 1:
        st.caption("✅ เหมาะสำหรับ: ยุทธศาสตร์/การกำหนดนโยบายเบื้องต้น")
    else:
        st.caption("✅ เหมาะสำหรับ: การคำนวณงบประมาณ, การจัดทำผังเมือง และการออกแบบทางวิศวกรรม")

def context_header(problem, concept):
    st.markdown(f"""
    <div class="context-box">
        <strong>ปัญหา:</strong> {problem}<br>
        <strong>แนวคิด:</strong> {concept}
    </div>
    """, unsafe_allow_html=True)

# --- MVP-1: Policy Briefing Service ---
if mvp_selection == mvp_labels["MVP-1"]:
    st.header("MVP-1: บริการสรุปนโยบาย (Policy Briefing)")
    context_header(
        "ผู้วางแผนในพื้นที่ไม่สามารถแปลงข้อมูลตัวเลข (เช่น +2°C) ให้เป็นการปฏิบัติเชิงบริหารได้",
        "ระบบสร้างข้อสรุปอัตโนมัติ (Briefing Generator) ที่แปลงข้อมูลเชิงเทคนิคให้เป็นรายงานสรุป"
    )
    
    is_ideal = level_toggle()
    st.markdown("---")
    
    if not is_ideal:
        st.markdown("### ระดับปฏิบัติ (L1): การวางยุทธศาสตร์")
        decision_label_component(1)
        
        with st.container(border=True):
            st.markdown("### 📊 รายงานสรุปความเสี่ยงรายจังหวัด: เชียงใหม่ (Climate Risk Scorecard)")
            st.caption("พ.ศ. 2570 - 2590 | ระดับความเชื่อมั่นภาพรวม: High (อ้างอิง CMIP6)")
            
            # Header Row
            h1, h2, h3, h4 = st.columns([1.5, 1, 3, 3])
            with h1: st.markdown("**ประเภทภัย**")
            with h2: st.markdown("**ความเชื่อมั่น**")
            with h3: st.markdown("**ผลกระทบสำคัญ**")
            with h4: st.markdown("**ข้อเสนอการปรับตัว**")
            st.divider()

            # Row 1: Flood
            r1_c1, r1_c2, r1_c3, r1_c4 = st.columns([1.5, 1, 3, 3])
            with r1_c1: st.markdown("🌊 **น้ำท่วม (Flood)**\n\n🔴 *เร่งด่วน*")
            with r1_c2: st.markdown("⭐⭐⭐\n\n(High)")
            with r1_c3: st.markdown("พื้นที่เศรษฐกิจริมน้ำปิง/เขตเมืองเก่า เสี่ยงน้ำท่วมฉับพลันเพิ่มขึ้น 20%")
            with r1_c4: st.markdown("พัฒนาพื้นที่แก้มลิงธรรมชาติ (NbS) และปรับปรุงระบบระบายน้ำเขตเมือง")
            st.divider()

            # Row 2: Drought
            r2_c1, r2_c2, r2_c3, r2_c4 = st.columns([1.5, 1, 3, 3])
            with r2_c1: st.markdown("🍂 **ภัยแล้ง (Drought)**\n\n🟡 *ปานกลาง*")
            with r2_c2: st.markdown("⭐⭐\n\n(Medium)")
            with r2_c3: st.markdown("พื้นที่เกษตรนอกเขตชลประทาน (จอมทอง, ฮอด) ขาดแคลนน้ำยาวนานขึ้น")
            with r2_c4: st.markdown("ส่งเสริมพืชใช้น้ำน้อย และพัฒนาระบบกักเก็บน้ำระดับไร่นา (Farm Pond)")
            st.divider()

            # Row 3: Heat
            r3_c1, r3_c2, r3_c3, r3_c4 = st.columns([1.5, 1, 3, 3])
            with r3_c1: st.markdown("🌡️ **ความร้อน (Heat)**\n\n🟡 *ปานกลาง*")
            with r3_c2: st.markdown("⭐⭐⭐\n\n(High)")
            with r3_c3: st.markdown("ปรากฏการณ์เกาะความร้อนเมือง (UHI) กระทบสุขภาพกลุ่มเปราะบาง")
            with r3_c4: st.markdown("เพิ่มพื้นที่สีเขียวในเมือง และออกแบบอาคารลดการใช้พลังงาน")
            st.divider()

            # Row 4: Landslide
            r4_c1, r4_c2, r4_c3, r4_c4 = st.columns([1.5, 1, 3, 3])
            with r4_c1: st.markdown("🏔️ **ดินถล่ม (Landslide)**\n\n🔴 *เร่งด่วน*")
            with r4_c2: st.markdown("⭐\n\n(Low)")
            with r4_c3: st.markdown("พื้นที่ลาดชัน (ฝาง, แม่อาย) เสี่ยงดินถล่มจากฝนสุดขีด")
            with r4_c4: st.markdown("ติดตั้งระบบเตือนภัยล่วงหน้า และฟื้นฟูป่าต้นน้ำธรรมชาติ")

    else:
        st.markdown("### ระดับอุดมคติ (L2): การออกแบบทางเทคนิค")
        decision_label_component(2)
        
        st.info("💡 ข้อมูลละเอียดสูงที่เชื่อมโยงกับค่าความปลอดภัย (Safety Factor) ของโครงสร้างพื้นฐาน")
        
        col_a, col_b, col_c = st.columns(3)
        with col_a:
            st.metric("จำนวนวันร้อนจัด (Extremely Hot Days)", "+25%", delta="สำหรับปี 2050")
        with col_b:
            st.metric("ค่าการเผื่อปริมาณฝน (Rainfall Allowance)", "+20%", delta="สำหรับการออกแบบท่อระบายน้ำ")
        with col_c:
            st.metric("อุณหภูมิสูงสุด (Max Temperature)", "+3 °C", delta="สำหรับงานวิศวกรรมอาคาร")

# --- MVP-2: Climate Disaster Statistics ---
elif mvp_selection == mvp_labels["MVP-2"]:
    st.header("MVP-2: สถิติภัยพิบัติภูมิอากาศ (Disaster Stats)")
    context_header(
        "ข้อมูลภัยพิบัติมักเน้นเพื่อการสงเคราะห์ (Relief) แต่ผู้วางแผนต้องการข้อมูลเพื่อพิสูจน์การลงทุน (ROI)",
        "ระบบเชื่อมโยงงบสงเคราะห์กับรอบอุบัติซ้ำของภัยภูมิอากาศเพื่อแปลงเป็นหลักฐานความเสียหาย"
    )
    
    is_ideal = level_toggle()
    st.markdown("---")
    
    years = list(range(2005, 2026))
    districts = ["อำเภอ เมือง", "อำเภอ บางบาล", "อำเภอ เสนา", "อำเภอ ผักไห่"]
    sectors = ["เกษตรกรรม", "โครงสร้างพื้นฐาน", "ที่อยู่อาศัย", "สาธารณสุข"]
    
    if not is_ideal:
        st.markdown("### ระดับปฏิบัติ (L1): การบูรณาการข้อมูลเบื้องต้น")
        st.warning("แสดงงบประมาณการเยียวยาแยกตามพื้นที่และกลุ่มภารกิจ")
        
        c1, c2 = st.columns(2)
        with c1:
            df_dist = pd.DataFrame({'พื้นที่': districts, 'งบประมาณ (ล้านบาท)': [450, 890, 620, 310]})
            fig1 = px.bar(df_dist, x='พื้นที่', y='งบประมาณ (ล้านบาท)', title="งบเยียวยาภัยพิบัติสะสม 20 ปี (แยกตามพื้นที่)")
            st.plotly_chart(fig1, use_container_width=True)
        with c2:
            df_sect = pd.DataFrame({'ภาคส่วน': sectors, 'งบประมาณ (ล้านบาท)': [1200, 560, 420, 90]})
            fig2 = px.pie(df_sect, values='งบประมาณ (ล้านบาท)', names='ภาคส่วน', title="สัดส่วนงบเยียวยา (แยกตามภาคส่วน)")
            st.plotly_chart(fig2, use_container_width=True)
        
    else:
        st.markdown("### ระดับอุดมคติ (L2): มูลค่าความเสียหายจริง (Monetary Loss)")
        st.success("แสดงมูลค่าความเสียหายที่ประเมินได้จริงและการเชื่อมโยงกับปรากฏการณ์ El Niño/La Niña")
        
        # Simulated Data for 20 years
        np.random.seed(42)
        total_loss = np.random.normal(1000, 300, len(years))
        pop_trend = np.linspace(1.2, 1.5, len(years)) # Population in millions
        
        # Highlight El Nino / La Nina
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=years, y=pop_trend * 1000, name="จำนวนประชากร (พันคน)", yaxis="y2", line=dict(color='gray', dash='dot')))
        fig.add_trace(go.Bar(x=years, y=total_loss, name="มูลค่าความเสียหายจริง (ล้านบาท)", marker_color='indianred'))
        
        fig.add_vrect(x0=2015, x1=2016, fillcolor="orange", opacity=0.3, layer="below", line_width=0, annotation_text="El Niño (ภัยแล้ง)")
        fig.add_vrect(x0=2010.5, x1=2011.5, fillcolor="blue", opacity=0.2, layer="below", line_width=0, annotation_text="มหาอุทกภัย")
        fig.add_vrect(x0=2020, x1=2022, fillcolor="blue", opacity=0.2, layer="below", line_width=0, annotation_text="La Niña")

        fig.update_layout(
            title="แนวโน้มความเสียหายรายปี (2005-2025) และปัจจัยกระตุ้น",
            xaxis_title="ปี พ.ศ.",
            yaxis_title="มูลค่าความเสียหาย (ล้านบาท)",
            yaxis2=dict(title="ประชากร", overlaying="y", side="right"),
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
        )
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("**การแยกแยะตามภาคส่วน (จริง):**")
        loss_data = pd.DataFrame({
            'ปี': [2023, 2023, 2023],
            'ภาคส่วน': ['เกษตร', 'ที่อยู่อาศัย', 'ธุรกิจ'],
            'ความเสียหายจริง (ล้าน)': [850, 320, 150]
        })
        st.dataframe(loss_data, use_container_width=True)

# --- MVP-3: Data Inventory ---
elif mvp_selection == mvp_labels["MVP-3"]:
    st.header("MVP-3: คลังข้อมูลความเสี่ยง (Data Inventory)")
    context_header(
        "มีข้อมูลจากหลายแหล่งและหลายเวอร์ชัน ทำให้ผู้ใช้ไม่แน่ใจว่าตัวไหนคือค่ามาตรฐานที่ควรนำไปใช้",
        "ระบบจัดแสดงข้อมูล (Gallery) ที่มีการคัดสรรและประทับตราการรับรองจาก DCCE"
    )
    
    is_ideal = level_toggle()
    st.markdown("---")
    
    datasets = [
        {
            "name": "ชุดข้อมูลฝนรายวันมาตรฐาน (TMD-TH-2024)",
            "agency": "กรมอุตุนิยมวิทยา",
            "tags": ["รายงานทางการ", "วิจัย", "นโยบาย"],
            "readiness": "Scoping, Budgeting",
            "badge": "DCCE Validated"
        },
        {
            "name": "แผนที่พื้นที่เสี่ยงภัยแล้งซ้ำซาก",
            "agency": "สทนช.",
            "tags": ["แผนแม่บท", "เกษตร", "ลุ่มน้ำ"],
            "readiness": "Scoping, Zoning",
            "badge": "DCCE Validated"
        },
        {
            "name": "ระดับน้ำทะเลหนุนสูงสุด (2050)",
            "agency": "ทล.",
            "tags": ["วิศวกรรม", "ชายฝั่ง"],
            "readiness": "Zoning, Design",
            "badge": "DCCE Validated"
        }
    ]
    
    if not is_ideal:
        st.markdown("### ระดับปฏิบัติ (L1): การคัดสรรข้อมูล (Curation)")
        st.warning("Decision support: 'ชุดข้อมูลใดคือค่ามาตรฐานที่ต้องใช้ในการรายงาน?'")
    else:
        st.markdown("### ระดับอุดมคติ (L2): การสืบค้นแบบบูรณาการ (Integration)")
        st.success("Decision support: 'ข้อมูลตัวใดมีความแม่นยำและเหมาะสมที่สุดกับโจทย์ทางเทคนิค?'")

    # Display datasets in a grid
    cols = st.columns(3)
    for i, d in enumerate(datasets):
        with cols[i % 3].container(border=True):
            st.write(f"#### {d['name']}")
            st.caption(f"แหล่งที่มา: {d['agency']} | สถานะ: :green[{d['badge']}]")
            
            # Tags row
            st.markdown(" ".join([f"`{tag}`" for tag in d['tags']]))
            
            st.info(f"📍 การใช้งานที่แนะนำ: {d['readiness']}")
            if is_ideal:
                st.markdown("---")
                st.caption("**Lineage:** Raw Stations + AI QA")

# --- MVP-4: Uncertainty Guide ---
elif mvp_selection == mvp_labels["MVP-4"]:
    st.header("MVP-4: คู่มือการตีความ (Uncertainty Guide)")
    context_header(
        "การนำข้อมูลหยาบไปใช้ในการออกแบบที่ต้องการความแม่นยำสูง นำไปสู่ความเสี่ยงและการลงทุนที่ผิดพลาด",
        "ระบบ Decision Guardrails ที่ระบุระดับความพร้อมของข้อมูลต่อประเภทภารกิจที่แตกต่างกัน"
    )
    
    is_ideal = level_toggle()
    st.markdown("---")
    
    # Selection of Dataset
    st.markdown("### 🔍 ขั้นตอนที่ 1: เลือกชุดข้อมูลที่ต้องการตรวจสอบ")
    selected_data = st.selectbox(
        "ชุดข้อมูล (Data Product):",
        [
            "แผนที่ความเสี่ยงอุทกภัยระดับจังหวัด (12km Grid)", 
            "แบบจำลองฝนระดับท้องถิ่น (1km Grid - Endorsed)", 
            "สถิติความแล้งสะสมราย 10 ปี (Observational)"
        ]
    )
    
    # Logic for Confidence per selection
    confidence_map = {
        "แผนที่ความเสี่ยงอุทกภัยระดับจังหวัด (12km Grid)": ["green", "amber", "red", "red"],
        "แบบจำลองฝนระดับท้องถิ่น (1km Grid - Endorsed)": ["green", "green", "green", "amber"],
        "สถิติความแล้งสะสมราย 10 ปี (Observational)": ["green", "green", "amber", "red"]
    }
    
    conf = confidence_map[selected_data]
    
    st.markdown("### 📊 ขั้นตอนที่ 2: ระดับความเหมาะสมต่อภารกิจ (Decision Readiness Matrix)")
    
    # 4 Use Case Blocks
    c1, c2, c3, c4 = st.columns(4)
    
    with c1:
        st.markdown(f'<div class="status-{conf[0]}">🎯 <strong>ยุทธศาสตร์</strong><br><small>Scoping</small></div>', unsafe_allow_html=True)
        with st.container(border=True):
            st.write("**ความเหมาะสม:**")
            if conf[0] == "green": st.write("✅ ใช้งานได้ทันที")
            st.caption("ใช้ระบุพื้นที่เป้าหมายและจัดลำดับความสำคัญระดับนโยบาย")
            
    with c2:
        st.markdown(f'<div class="status-{conf[1]}">💰 <strong>งบประมาณ</strong><br><small>Budgeting</small></div>', unsafe_allow_html=True)
        with st.container(border=True):
            st.write("**ความเหมาะสม:**")
            if conf[1] == "green": st.write("✅ ใช้งานได้")
            elif conf[1] == "amber": st.write("⚠️ ควรมีค่าเผื่อ (Buffer)")
            st.caption("ใช้ในการจองงบประมาณรายปีและการวางแผนโครงการเบื้องต้น")

    with c3:
        st.markdown(f'<div class="status-{conf[2]}">🗺️ <strong>ผังเมือง</strong><br><small>Zoning</small></div>', unsafe_allow_html=True)
        with st.container(border=True):
            st.write("**ความเหมาะสม:**")
            if conf[2] == "green": st.write("✅ ใช้งานได้")
            elif conf[2] == "amber": st.write("⚠️ ต้องตรวจสอบเพิ่ม")
            elif conf[2] == "red": st.write("❌ ไม่แนะนำ")
            st.caption("ใช้ในการกำหนดเขตควบคุมอาคารและกฎหมายผังเมือง")

    with c4:
        st.markdown(f'<div class="status-{conf[3]}">🏗️ <strong>การออกแบบ</strong><br><small>Design</small></div>', unsafe_allow_html=True)
        with st.container(border=True):
            st.write("**ความเหมาะสม:**")
            if conf[3] == "amber": st.write("⚠️ ใช้เฉพาะจุด (Site-Specific)")
            elif conf[3] == "red": st.write("❌ ไม่แนะนำ")
            st.caption("ใช้คำนวณสเปควิศวกรรมและความแข็งแรงของโครงสร้าง")

    st.markdown("---")
    
    if is_ideal:
        st.markdown("### ระดับอุดมคติ (L2): รายงานระเบียบวิธีและอินโฟกราฟิก")
        st.success("เอกสารอธิบายเกณฑ์การให้คะแนนความเชื่อมั่น (Confidence Rating Methodology)")
        
        with st.expander("📝 ดูรายละเอียดระเบียบวิธี (Methodology Report)"):
            st.write(f"วิเคราะห์ความไม่แน่นอนของ **{selected_data}**")
            st.write("เกณฑ์การตัดสินใจอ้างอิงตาม IPCC AR6 Confidence Lexicon:")
            st.image("https://via.placeholder.com/1000x300?text=Confidence+Rating+Methodology+Infographic")

st.markdown("---")
st.caption("พัฒนาโดย ARUN (Oracle) เพื่อใช้ประกอบการประชุมเชิงปฏิบัติการ CRDB/NCAIF")
