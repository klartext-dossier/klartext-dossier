import io, klartext

input = io.StringIO("""
process: #SD.2 name="Software Development Planning"

    purpose:
        The _objective_ of the "Software Development Planning" process 
        is to plan the software development tasks, communicate procedures 
        and goals to members of the development team.

        Systematic software development planning ensures that risks caused 
        by software are reduced and quality characteristics for the medical 
        device software are met.
""")

parser = klartext.Parser()

xml = parser.parse(input, convert_text=klartext.Parser.convertMarkdown)

print(xml.decode('UTF-8'))

