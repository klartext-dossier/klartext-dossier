!import "http://klartext-dossier.org/medical-device-file" as md
!import "http://klartext-dossier.org/ops-2025" as ops
!import "http://klartext-dossier.org/icd-10-gm" as icd
!import "http://hoelzer-kluepfel.de/generic-dialysis-system" as gds


md::intended-use: #gds-intended-use

    md::intended-use-summary:
        The /r/device/ is a {gds::dialysis machine} providing {gds::haemodialysis} treatments for patients with {gds::permanent kidney failure}.

    md::medical-purpose:
        The /r/device/ provides a renal replacement therapy with the following {gds::clinical functions}:
        
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
      