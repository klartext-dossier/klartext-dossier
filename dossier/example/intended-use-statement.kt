!import "http://www.klartext-dossier.org/medical-device-file" as md
!import "http://www.klartext-dossier.org/ops-2025" as ops
!import "http://www.klartext-dossier.org/icd-10-gm" as icd

md::intended-use: #gds-intended-use

    md::intended-use-summary:
        The /r/device/ is a {dialysis machine} providing {haemodialysis} treatments for /r/patient/s with {permanent kidney failure}.

    md::medical-purpose:
        The /r/device/ provides a renal replacement therapy with the following {clinical functions}:
        
        md::clinical-function: name="Ultrafiltration"
            Removal of substances with low {molecular weight} from the /r/patient/'s blood

        md::clinical-function: name="Net Fluid Removal"
            Removal of excess water from the /r/patient/'s blood

        ops::ops-code> ops::code-8-854.x

    md::medical-indication:
        /r/patient/s with {permanent kidney failure} and low {glomerular filtration rate} (GFR < 15 mL/min).

        icd::icd-code> icd::code-N18.5
        icd::icd-code> icd::code-Z99.2
        
    md::patient-group: #patient name="Patient"
        Patients with {permanent kidney failure} and a {body-weight} > 40 kg.

    md::intended-user: #physician name="Nephrologist"

    md::intended-user: #nurse name="Dialysis Nurse"

    md::intended-user: #technician name="Medical Technician"

    md::use-environment: #ward name="Hospital Ward"
      