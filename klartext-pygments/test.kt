!include "includefile.kt"
!import "http://www.klartext-dossier.org" as org

single: Some _Content_

org::nocontent:
    tag:
        sada

org::link> ID key="value"

// This is a comment
    // And this too
    
one: #ID [de] content 1
    two: #id another-key="anothervalue" content 2
        three: content 3

one-more: #ID _content 1_
    twomore: #id key="value" "content 2"
        threemore: content 3
    
tag:
    # Heading

    This *is* simple _markdown_.

tag: #org::ident

link> org::ident [en]
