<map version="freeplane 1.7.0">
<!--To view this file, download free mind mapping software Freeplane from http://freeplane.sourceforge.net -->
<node TEXT="Dossier" FOLDED="false" ID="ID_1970501493" CREATED="1614592857105" MODIFIED="1614592910926" STYLE="oval">
<font SIZE="18"/>
<hook NAME="MapStyle">
    <properties edgeColorConfiguration="#808080ff,#ff0000ff,#0000ffff,#00ff00ff,#ff00ffff,#00ffffff,#7c0000ff,#00007cff,#007c00ff,#7c007cff,#007c7cff,#7c7c00ff" fit_to_viewport="false"/>

<map_styles>
<stylenode LOCALIZED_TEXT="styles.root_node" STYLE="oval" UNIFORM_SHAPE="true" VGAP_QUANTITY="24.0 pt">
<font SIZE="24"/>
<stylenode LOCALIZED_TEXT="styles.predefined" POSITION="right" STYLE="bubble">
<stylenode LOCALIZED_TEXT="default" ICON_SIZE="12.0 pt" COLOR="#000000" STYLE="fork">
<font NAME="SansSerif" SIZE="10" BOLD="false" ITALIC="false"/>
</stylenode>
<stylenode LOCALIZED_TEXT="defaultstyle.details"/>
<stylenode LOCALIZED_TEXT="defaultstyle.attributes">
<font SIZE="9"/>
</stylenode>
<stylenode LOCALIZED_TEXT="defaultstyle.note" COLOR="#000000" BACKGROUND_COLOR="#ffffff" TEXT_ALIGN="LEFT"/>
<stylenode LOCALIZED_TEXT="defaultstyle.floating">
<edge STYLE="hide_edge"/>
<cloud COLOR="#f0f0f0" SHAPE="ROUND_RECT"/>
</stylenode>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.user-defined" POSITION="right" STYLE="bubble">
<stylenode LOCALIZED_TEXT="styles.topic" COLOR="#18898b" STYLE="fork">
<font NAME="Liberation Sans" SIZE="10" BOLD="true"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.subtopic" COLOR="#cc3300" STYLE="fork">
<font NAME="Liberation Sans" SIZE="10" BOLD="true"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.subsubtopic" COLOR="#669900">
<font NAME="Liberation Sans" SIZE="10" BOLD="true"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.important">
<icon BUILTIN="yes"/>
</stylenode>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.AutomaticLayout" POSITION="right" STYLE="bubble">
<stylenode LOCALIZED_TEXT="AutomaticLayout.level.root" COLOR="#000000" STYLE="oval" SHAPE_HORIZONTAL_MARGIN="10.0 pt" SHAPE_VERTICAL_MARGIN="10.0 pt">
<font SIZE="18"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,1" COLOR="#0033ff">
<font SIZE="16"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,2" COLOR="#00b439">
<font SIZE="14"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,3" COLOR="#990000">
<font SIZE="12"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,4" COLOR="#111111">
<font SIZE="10"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,5"/>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,6"/>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,7"/>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,8"/>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,9"/>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,10"/>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,11"/>
</stylenode>
</stylenode>
</map_styles>
</hook>
<hook NAME="AutomaticEdgeColor" COUNTER="8" RULE="ON_BRANCH_CREATION"/>
<hook NAME="accessories/plugins/AutomaticLayout.properties" VALUE="ALL"/>
<node TEXT="Documentation as Code" POSITION="right" ID="ID_1650286680" CREATED="1614592885137" MODIFIED="1614592902240">
<edge COLOR="#ff0000"/>
<node TEXT="Version controlled" ID="ID_1643301404" CREATED="1614592970931" MODIFIED="1614592976974">
<node TEXT="git" ID="ID_1741056745" CREATED="1614592978580" MODIFIED="1614592980587"/>
</node>
</node>
<node TEXT="Multiple output generators" POSITION="right" ID="ID_514980172" CREATED="1614592927206" MODIFIED="1614592965669">
<edge COLOR="#0000ff"/>
<node TEXT="PDF" ID="ID_1131499766" CREATED="1614592935252" MODIFIED="1614592937272"/>
<node TEXT="HTML" ID="ID_547900154" CREATED="1614592937724" MODIFIED="1614592939624"/>
</node>
<node TEXT="Text-based documentation formats" FOLDED="true" POSITION="right" ID="ID_1488778970" CREATED="1614592912369" MODIFIED="1614592967889">
<edge COLOR="#00ff00"/>
<node TEXT="klartext" ID="ID_1972105025" CREATED="1614593027835" MODIFIED="1614593031206"/>
<node TEXT="markdown" ID="ID_869202633" CREATED="1614593031607" MODIFIED="1614593034656"/>
</node>
<node TEXT="Standards based" POSITION="right" ID="ID_1856463560" CREATED="1614593165998" MODIFIED="1614593224061">
<edge COLOR="#00007c"/>
<node TEXT="XML" ID="ID_1382841689" CREATED="1614593174994" MODIFIED="1614593176675"/>
<node TEXT="XHTML" ID="ID_690527235" CREATED="1614593177937" MODIFIED="1614593180337"/>
<node TEXT="CSS" ID="ID_660942669" CREATED="1614593180541" MODIFIED="1614593182321"/>
<node TEXT="XSLT" ID="ID_748747281" CREATED="1614593183610" MODIFIED="1614593185433"/>
</node>
<node TEXT="Information extraction" POSITION="right" ID="ID_736980601" CREATED="1614593003674" MODIFIED="1614593007874">
<edge COLOR="#ff00ff"/>
<node TEXT="create information items from other sources" ID="ID_548705984" CREATED="1614593008759" MODIFIED="1614593020235">
<node TEXT="source code" ID="ID_1438949762" CREATED="1614593272492" MODIFIED="1614593279150"/>
<node TEXT="pipeline definition" ID="ID_1224331471" CREATED="1614593279596" MODIFIED="1614593284058"/>
</node>
<node TEXT="extensible plugins" ID="ID_1353989422" CREATED="1614593286065" MODIFIED="1614593292769"/>
</node>
<node TEXT="Styling" POSITION="right" ID="ID_1271153921" CREATED="1614593049405" MODIFIED="1614593051672">
<edge COLOR="#00ffff"/>
<node TEXT="separate presentation from content" ID="ID_176259672" CREATED="1614593052427" MODIFIED="1614593059760"/>
</node>
<node TEXT="Multiple tools" POSITION="right" ID="ID_1456786552" CREATED="1614593074469" MODIFIED="1614593078906">
<edge COLOR="#7c0000"/>
<node TEXT="plugins into IDEs" ID="ID_1002144955" CREATED="1614593079690" MODIFIED="1614593085373">
<node TEXT="VSCode" ID="ID_1973995688" CREATED="1614593100558" MODIFIED="1614593102572"/>
</node>
<node TEXT="plugins into build pipelines" FOLDED="true" ID="ID_61289919" CREATED="1614593085822" MODIFIED="1614593095589">
<node TEXT="Azure" ID="ID_994062362" CREATED="1614593096498" MODIFIED="1614593098054"/>
</node>
<node TEXT="Web-based editor" ID="ID_350729679" CREATED="1614593196472" MODIFIED="1614593200554"/>
<node TEXT="Desktop editor" ID="ID_1038648005" CREATED="1614593201121" MODIFIED="1614593207689"/>
</node>
<node TEXT="Services" POSITION="right" ID="ID_188430020" CREATED="1614600320673" MODIFIED="1614600323705">
<edge COLOR="#007c00"/>
<node TEXT="online document generation" ID="ID_734366141" CREATED="1614600324608" MODIFIED="1614600340963"/>
<node TEXT="online editing plattform" ID="ID_549636182" CREATED="1614600341893" MODIFIED="1614600349494"/>
<node TEXT="template and stylesheet creation" ID="ID_485175261" CREATED="1614600350182" MODIFIED="1614600369622"/>
</node>
</node>
</map>
