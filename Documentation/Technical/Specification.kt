specification: 

    system: #system-dossier name="Dossier"

        /r.q/product-dossier/ is a system to author technical documentation.

        requirement: 
            The system allows the user to author technical documentation based on technologies common in software development.


        component: #component-klartext name="klartext"

            /r.q/component-klartext/ is a markup language for structured technical documentation.

            requirement:
                The markup language allows the user to define a nested structure of {tags}.

            requirement:
                The markup language allows the user to define an unlimited number of attributes for each {tag}.


        component: #component-dm name="dm"

            /r.q/component-dm/ is a software to process documentation sources.

            requirement: 
                The software allows the user to convert {input documents} in {klartext format} into {output documents} in {PDF format}.

