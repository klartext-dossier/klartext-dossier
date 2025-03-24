!include "includefile.kt"
!import "http://www.klartext-dossier.org" as org

single: Some _Content_

org::nocontent:
    tag:
        sada

org::link> ID key="value"

// This is a comment
    // And this too
    
one: #ID content 1
    two: #id key="value" anotherkey="anothervalue" content 2
        three: content 3

onemore: #ID _content 1_
    twomore: #id key="value" content 2
        threemore: content 3
    
tag:
    # Heading

    This *is* simple _markdown_.