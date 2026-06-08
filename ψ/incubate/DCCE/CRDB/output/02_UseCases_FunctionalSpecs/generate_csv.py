import json
import csv
import os

json_file = 'ψ/incubate/DCCE/CRDB/output/02_UseCases_FunctionalSpecs/P2_Hard_Dependencies_Inventory.json'
csv_file = 'ψ/incubate/DCCE/CRDB/output/02_UseCases_FunctionalSpecs/NCAIF_Use_Case_Traceability_Matrix_v2.0.csv'

with open(json_file, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Helper for description generation
def generate_desc_en(item):
    agency = item.get('agency', 'the agency')
    use_case = item.get('use_case', 'this task')
    triggers = ", ".join(item.get('triggers', [])) if item.get('triggers') else 'institutional mandates'
    variables = ", ".join(item.get('data_parameters', {}).get('variables', [])) if item.get('data_parameters', {}).get('variables') else 'specific metrics'
    res = item.get('data_parameters', {}).get('resolution', 'variable')
    
    desc = f"This use case is designed for {agency} to facilitate the '{use_case}'. It is primarily driven by decision moments such as {triggers}. The service provides critical intelligence products, requiring specific data parameters including {variables} at a {res} resolution. Ultimately, this ensures that the agency can effectively execute its mandates with officially verified evidence."
    return desc

def generate_desc_th(item):
    agency = item.get('agency', 'หน่วยงาน')
    use_case = item.get('use_case', 'งานนี้')
    
    # Simple mapping for agencies to Thai for better flow
    agency_map = {
        "DCCE": "กรมการเปลี่ยนแปลงสภาพภูมิอากาศและสิ่งแวดล้อม (DCCE)",
        "TBA": "สมาคมธนาคารไทย (TBA)",
        "OTP": "สำนักงานนโยบายและแผนการขนส่งและจราจร (สนข.)",
        "DPT": "กรมโยธาธิการและผังเมือง (ยผ.)",
        "NESDC": "สำนักงานสภาพัฒนาการเศรษฐกิจและสังคมแห่งชาติ (สภาพัฒน์)",
        "NXPO": "สำนักงานสภานโยบายการอุดมศึกษา วิทยาศาสตร์ วิจัยและนวัตกรรมแห่งชาติ (สอวช.)",
        "FTI": "สภาอุตสาหกรรมแห่งประเทศไทย (ส.อ.ท.)",
        "MSDHS": "กระทรวงการพัฒนาสังคมและความมั่นคงของมนุษย์ (พม.)",
        "BMA": "กรุงเทพมหานคร (กทม.)",
        "DLA": "กรมส่งเสริมการปกครองท้องถิ่น (สถ.)",
        "DDPM": "กรมป้องกันและบรรเทาสาธารณภัย (ปภ.)",
        "NSO": "สำนักงานสถิติแห่งชาติ (สสช.)",
        "DOH": "กรมอนามัย",
        "ONEP": "สำนักงานนโยบายและแผนทรัพยากรธรรมชาติและสิ่งแวดล้อม (สผ.)",
        "DGA": "สำนักงานพัฒนารัฐบาลดิจิทัล (สพร.)",
        "UDDC": "ศูนย์ออกแบบและพัฒนาเมือง (UDDC)"
    }
    
    agency_th = agency_map.get(agency, agency)
    triggers = ", ".join(item.get('triggers', [])) if item.get('triggers') else 'ข้อกำหนดทางสถาบัน'
    variables = ", ".join(item.get('data_parameters', {}).get('variables', [])) if item.get('data_parameters', {}).get('variables') else 'ตัวชี้วัดเฉพาะ'
    res = item.get('data_parameters', {}).get('resolution', 'ระดับที่เหมาะสม')
    
    desc = f"กรณีการใช้งานนี้ถูกออกแบบมาสำหรับ {agency_th} เพื่อสนับสนุนการดำเนินงานด้าน '{use_case}' โดยมีเงื่อนไขสำคัญที่กระตุ้นให้เกิดการตัดสินใจคือ {triggers} ระบบจะส่งมอบข้อมูลอัจฉริยะที่ประกอบด้วย {variables} ในระดับความละเอียด {res} เพื่อให้หน่วยงานสามารถปฏิบัติภารกิจและตัดสินใจเชิงนโยบายหรือปฏิบัติการได้อย่างมีประสิทธิภาพ บนพื้นฐานของข้อมูลที่ได้รับการรับรองความถูกต้อง"
    return desc

with open(csv_file, 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['UC ID', 'Service Group', 'Agency', 'Use Case / Decision Moment', 'Key Technical Specs', 'Source Anchors', 'Description (EN)', 'Description (TH)'])
    
    for item in data:
        uc_id = item.get('id', '')
        service_id = item.get('service_id', '')
        agency = item.get('agency', '')
        use_case = item.get('use_case', '')
        
        tech_specs = f"Variables: {', '.join(item.get('data_parameters', {}).get('variables', []))} | Resolution: {item.get('data_parameters', {}).get('resolution', '')}"
        anchors = ", ".join(item.get('source_anchors', []))
        
        desc_en = generate_desc_en(item)
        desc_th = generate_desc_th(item)
        
        writer.writerow([uc_id, service_id, agency, use_case, tech_specs, anchors, desc_en, desc_th])

print("CSV generated successfully.")
