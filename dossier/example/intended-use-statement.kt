!import "http://www.klartext-dossier.org/medical-device-file" as md
!import "http://www.klartext-dossier.org/ops-2025" as ops
!import "http://www.klartext-dossier.org/icd-10-gm" as icd

md::intended-use: #gds-intended-use

    md::intended-use-summary:
        The /r/DEVICE/ is a dialysis machine providing haemodialysis treatments.

    md::medical-purpose:
        The /r/DEVICE/ provides a renal replacement therapy with the following clinical functions:
        
        - Removal of substances with low molecular weight
        - Removal of excess water

        ops> ops::code-8-854.x

    md::medical-indication:
        Patients with symptomatic kidney failure and low glomerular filtration rate (GFR < 15 mL/min).

        icd> icd::code-N18.5
        
    md::patient-group:
        The /r/DEVICE/ is intended for patients with permanent kidney failure and a body-weight > 40 kg.

    md::intended-user: #physician name="Nephrologist"

    md::intended-user: #nurse name="Dialysis Nurse"

    md::intended-user: #technician name="Medical Technician"

    md::use-environment: #ward name="Hospital Ward"
      