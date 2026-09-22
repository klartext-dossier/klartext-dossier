!import "http://klartext-dossier.org/medical-device-file" as md
!import "http://klartext-dossier.org/ops-2025" as ops
!import "http://klartext-dossier.org/icd-10-gm" as icd
!import "http://hoelzer-kluepfel.de/generic-dialysis-system" as gds


md::intended-use: #gds-intended-use

    md::intended-use-summary:
        The /r/device/ is intended to perform extracorporeal blood purification treatment for patients with acute or {gds::permanent kidney failure}, or other conditions requiring renal replacement therapy. The device circulates the patient's blood through an extracorporeal circuit containing a dialyser (artificial kidney), where diffusion and ultrafiltration processes remove waste products, toxins, and excess fluids, and assist in maintaining electrolyte and acid-base balance.

    md::medical-purpose:
        The purpose of the /r/device/ is to support or replace the kidney's natural function in removing metabolic waste products, toxins, and excess fluid from the blood, and to assist in maintaining normal electrolyte and acid-base balance.

        md::clinical-function: name="Ultrafiltration"
            Removal of substances with low {gds::molecular weight} from the patient's blood

        md::clinical-function: name="Net Fluid Removal"
            Removal of excess water from the patient's blood

        ops::ops-code> ops::code-8-854.x

    md::medical-indication:
        /r/patient/ with {gds::permanent kidney failure} and low {gds::glomerular filtration rate} ({gds::GFR} < 15 mL/min).

        icd::icd-code> icd::code-N18.5
        icd::icd-code> icd::code-Z99.2
        
    md::patient-group: #patient name="Adult Patients"
        Patients with {gds::permanent kidney failure} and a body-weight > 40 kg.

    md::intended-user: #physician name="Nephrologist"

    md::intended-user: #nurse name="Dialysis Nurse"

    md::intended-user: #technician name="Medical Technician"

    md::use-environment: #ward name="Hospital Ward"
      