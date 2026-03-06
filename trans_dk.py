import sys

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

replacements = {
    'lang="de"': 'lang="da"',
    'Slimanol Erfahrungen & Bewertung: Inhaltsstoffe der Kapsel und Zusammensetzung': 'Slimanol Anmeldelser & Erfaringer: Kapslens Ingredienser og Sammensætning',
    'Slimanol Kapsel Erfahrungen: Bewertung der Inhaltsstoffe und Zusammensetzung': 'Slimanol Kapsel Erfaringer: Vurdering af Ingredienser og Sammensætning',
    'Slimanol Bewertung & Erfahrungen: Entdecken Sie die Inhaltsstoffe der Kapsel (Chrom, Berberin, EGCG, Mariendistel). Liposomale Zusammensetzung ohne Nebenwirkung. Natürliches Nahrungsergänzungsmittel (ab 18 Jahren).': 'Slimanol Anmeldelse & Erfaringer: Opdag kapslens ingredienser (Krom, Berberin, EGCG, Marietidsel). Liposomal sammensætning uden bivirkninger. Naturligt kosttilskud (fra 18 år).',
    'Slimanol, Bewertung, Kapsel, Inhaltsstoffe, Slimanol Erfahrungen, Zusammensetzung, Nebenwirkung, Chrom, EGCG, Berberin, Mariendistel, Nahrungsergänzungsmittel': 'Slimanol, anmeldelse, kapsel, ingredienser, Slimanol erfaringer, sammensætning, bivirkninger, krom, EGCG, berberin, marietidsel, kosttilskud',

    '60-TAGE GELD-ZURÜCK-GARANTIE': '60-DAGES TILFREDSHEDSGARANTI',
    'SCHNELLE LIEFERUNG IN DIE EU': 'HURTIG LEVERING TIL EU',
    'SICHERE & DISKRETE ABWICKLUNG': 'SIKKER & DISKRET KASSE',

    '>Wie es funktioniert<': '>Sådan fungerer det<',
    '>Vorteile<': '>Fordele<',
    '>Bewertungen<': '>Anmeldelser<',
    '>Häufige Fragen<': '>Ofte stillede spørgsmål<',
    'Jetzt Bestellen <i': 'Bestil Nu <i',

    'Durchschnittliche Kundenbewertung 4.8': 'Gennemsnitlig kundebedømmelse 4.8',
    'Nr. 1 Natürliche Stoffwechsel-Formel': 'Nr. 1 Naturlig Stofskifte-Formel',
    'Hören Sie auf, gegen Ihren Stoffwechsel zu kämpfen. <br>\n                        <span class="italic text-brand-gold">Fett natürlich verbrennen.</span>': 'Stop med at kæmpe mod dit stofskifte. <br>\n                        <span class="italic text-brand-gold">Forbrænd fedt naturligt.</span>',

    'Stoffwechselunterstützung': 'Stofskiftestøtte',
    'Slimanol ist die kraftvolle, natürliche Formel, die entwickelt wurde, um Ihren Stoffwechsel zu reaktivieren, Blähungen zu reduzieren und anhaltende Energie ohne extreme Diäten zu liefern.': 'Slimanol er den kraftfulde, naturlige formel designet til at genaktivere dit stofskifte, reducere oppustethed og give vedvarende energi uden ekstreme diæter.',
    'Weniger Heißhunger. Nachhaltige Fettverbrennung. Natürliche Zusatzstoffe. <strong>Keine Stimulanzien. Kein Crash.</strong>': 'Færre cravings. Bæredygtig fedtforbrænding. Naturlige ingredienser. <strong>Ingen stimulanser. Intet crash.</strong>',

    'FETTVERBRENNUNG AKTIVIEREN': 'AKTIVER FEDTFORBRÆNDING',
    '60-Tage Garantie': '60-Dages Garanti',
    '100%\n                            Natürlich': '100%\n                            Naturlig',
    'EU-Zertifiziert': 'EU-Certificeret',

    '60 KAPSELN': '60 KAPSLER',

    'Verifizierte Bewertungen': 'Verificerede Anmeldelser',
    'Durchschn. Bewertung': 'Gns. Bedømmelse',
    'Berichten von mehr Energie': 'Rapporterer om mere energi',
    '60-Tage\n                    Geld-zurück-Garantie': '60-Dages\n                    Tilfredshedsgaranti',
    'Offizielle Lieferung\n                in\n                Ihr Land': 'Officiel Levering\n                til\n                Dit Land',
    'Wählen Sie Ihr Land,\n                um\n                die Verfügbarkeit und schnelle Lieferung zu bestätigen': 'Vælg Dit Land\n                for at\n                Bekræfte Tilgængelighed & Hurtig Levering',

    '>Deutschland<': '>Tyskland<',
    '>Dänemark<': '>Danmark<',
    '> Auf Lager<': '> På Lager<',

    'Sichere\n                    Abwicklung': 'Sikker\n                    Kasse',
    'Schnelle\n                    Lieferung in die EU': 'Hurtig\n                    Levering til EU',
    '60-Tage\n                    Geld-zurück-Garantie': '60-dages\n                    tilfredshedsgaranti',

    'Reaktivieren Sie die natürliche Fettverbrennungsmaschine Ihres Körpers': 'Genaktiver Din Krops Naturlige Fedtforbrændingsmaskine',
    'Slimanol arbeitet mit Ihrem Körper zusammen, um die wahren Ursachen eines langsamen Stoffwechsels, von Verdauungsbeschwerden und Energiemangel zu bekämpfen.': 'Slimanol samarbejder med din krop for at målrette de grundlæggende årsager til langsomt stofskifte, fordøjelsesbesvær og lav energi.',

    '>Reaktivierung des Stoffwechsels<': '>Stofskifte Genoplivning<',
    '>Unterstützt einen aktiven Stoffwechsel ab 35 und hilft Ihrem Körper, Nährstoffe in Energie umzuwandeln, anstatt sie als Fett zu speichern.<': '>Understøtter et aktivt stofskifte efter 35 år, og hjælper din krop med at omdanne næringsstoffer til energi i stedet for at lagre dem som fedt.<',

    '>Anhaltende tägliche Energie<': '>Vedvarende Daglig Energi<',
    '>Erleben Sie den ganzen Tag einen natürlichen, stetigen Energiefluss. Keine Unruhe, keine Nachmittagstiefs, nur pure Vitalität.<': '>Oplev en naturlig, stabil strøm af energi hele dagen. Ingen rysten, ingen eftermiddagscrashes, kun ren vitalitet.<',

    '>Appetitkontrolle<': '>Appetitkontrol<',
    '>Hilft, emotionales Essen und nächtliche Heißhungerattacken zu zügeln, sodass es leichter wird, gesündere Essgewohnheiten beizubehalten.<': '>Hjælper med at bremse følelsesmæssig spisning og natlige cravings, hvilket gør det lettere at holde fast i sundere spisevaner.<',

    '>Verdauungserleichterung<': '>Fordøjelseslindring<',
    '>Fördert eine optimale Verdauungsgesundheit und reduziert das Gefühl von Schwere, Unbehagen und Blähungen nach den Mahlzeiten erheblich.<': '>Fremmer optimal fordøjelsessundhed, og reducerer markant følelsen af tyngde, ubehag og oppustethed efter måltider.<',

    '>Gesundes Gewichtsgleichgewicht<': '>Sund Vægtbalance<',
    '>Erreichen Sie Ihre Ziele schrittweise und nachhaltig. Keine extremen Diäten oder unmögliche Routinen erforderlich.<': '>Opnå dine mål gradvist og bæredygtigt. Ingen ekstreme diæter eller umulige rutiner kræves.<',

    '>100% natürliche Formel<': '>100% Naturlig Formel<',
    '>Hergestellt aus klinisch untersuchten Extrakten.\n                        Hergestellt in zertifizierten Anlagen mit alleinigem Fokus auf Qualität und Sicherheit.<': '>Fremstillet med klinisk undersøgte ekstrakter.\n                        Produceret i certificerede faciliteter med rent fokus på kvalitet og sikkerhed.<',

    'Slimanol jetzt entdecken ': 'Opdag Slimanol Nu ',

    'Was unsere Kunden sagen': 'Hvad Vores Kunder Siger',
    'Echte Transformationen von Menschen, die beschlossen haben, die Kontrolle über ihren Stoffwechsel zu übernehmen.': 'Ægte transformationer fra folk, der besluttede at tage kontrol over deres stofskifte.',
    'Ich kämpfe seit Jahren mit meinem Gewicht. Seit ich Slimanol nehme, habe ich so viel mehr Energie und die ständigen Blähungen sind weg. Ein wahrer Lebensretter!': 'Jeg har kæmpet med min vægt i årevis. Siden jeg begyndte at tage Slimanol, har jeg meget mere energi, og den konstante oppustethed er væk. En sand livredder!',
    ', Verifizierte Käuferin': ', Verificeret Køber',
    ', Verifizierter Käufer': ', Verificeret Køber',
    'Endlich ein Produkt, das mich nicht unruhig macht. Ich fühle mich leichter, aktiver und meine Kleidung passt so viel besser. Sehr zu empfehlen.': 'Endelig et produkt, der ikke gør mig rystende. Jeg føler mig lettere, mere aktiv, og mit tøj passer så meget bedre. Kan varmt anbefales.',
    'Meine Heißhungerattacken sind nach der ersten Woche verschwunden. Ich nehme stetig ab, ohne das Gefühl zu haben, ständig hungrig zu sein.': 'Mine cravings forsvandt efter den første uge. Jeg taber mig støt uden at føle, at jeg sulter hele tiden.',

    'Preise ansehen ': 'Se Priser ',
    '>Häufig gestellte Fragen<': '>Ofte Stillede Spørgsmål<',
    '>Alles, was Sie über Slimanol wissen müssen.<': '>Alt hvad du behøver at vide om Slimanol.<',

    '>Was genau ist Slimanol?<': '>Hvad præcist er Slimanol?<',
    'Slimanol ist ein erstklassiges, natürliches Nahrungsergänzungsmittel zur Unterstützung der Stoffwechselfunktion, zur Steigerung des Energieniveaus und zur Förderung einer gesunden Gewichtskontrolle. Es nutzt fortschrittliche liposomale Technologie für eine bessere Aufnahme von Schlüsselnährstoffen.': 'Slimanol er et premium, naturligt kosttilskud designet til at understøtte stofskiftefunktionen, øge energiniveauerne og fremme sund vægtkontrol. Det udnytter avanceret liposomal teknologi for bedre optagelse af nøglenæringsstoffer.',

    '>Ist die Anwendung sicher?<': '>Er det sikkert at bruge?<',
    'Ja, absolut. Slimanol besteht aus 100% natürlichen, pflanzlichen Inhaltsstoffen. Es gibt keine aggressiven Chemikalien, schädlichen Stimulanzien oder künstlichen Zusatzstoffe. Dennoch empfehlen wir immer, vor der Einnahme eines neuen Nahrungsergänzungsmittels einen Arzt zu konsultieren.': 'Ja, absolut. Slimanol er formuleret med 100% naturlige, plantebaserede ingredienser. Der er ingen barske kemikalier, skadelige stimulanser eller kunstige tilsætningsstoffer. Vi anbefaler dog altid at konsultere en læge, før du starter på et nyt kosttilskud.',

    '>Wie nehme ich Slimanol ein?<': '>Hvordan tager jeg Slimanol?<',
    'Nehmen Sie täglich 2 Kapseln ein, idealerweise 20-30 Minuten vor Ihrer Hauptmahlzeit, mit einem vollen Glas Wasser. Für optimale Ergebnisse behalten Sie eine konsequente tägliche Einnahme für mindestens 60 Tage bei.': 'Tag 2 kapsler dagligt, ideelt 20-30 minutter før dit hovedmåltid, med et fuldt glas vand. For de bedste resultater bør du opretholde en konsekvent daglig brug i mindst 60 dage.',

    '>Was ist, wenn es bei mir nicht wirkt?<': '>Hvad hvis det ikke virker for mig?<',
    'Wir bieten eine volle 60-Tage Geld-zurück-Garantie. Wenn Sie mit Ihrer Transformation nicht vollkommen zufrieden sind, kontaktieren Sie einfach unser Support-Team innerhalb von 60 Tagen nach dem Kauf und wir erstatten jeden Cent – ohne Fragen zu stellen.': 'Vi tilbyder en fuld 60-Dages Tilfredshedsgaranti. Hvis du ikke er fuldt tilfreds med din transformation, skal du blot kontakte vores supportteam inden for 60 dage efter købet, og vi refunderer hver en krone – uden at stille spørgsmål.',

    '>Wohin liefern Sie?<': '>Hvor leverer I?<',
    'Wir liefern sicher direkt an Kunden in Deutschland und Dänemark. Alle Bestellungen werden innerhalb von 24 Stunden bearbeitet und mit schnellen, zuverlässigen Kurieren in diskreter Verpackung versendet.': 'Vi leverer sikkert direkte til kunder i Tyskland og Danmark. Alle ordrer behandles inden for 24 timer og sendes med hurtige, pålidelige kurerer i diskret emballage.',

    'Slimanol Kapseln: Erfahrungen und Bewertungen zum Inhaltsstoffe Test': 'Slimanol Kapsler: Erfaringer og Anmeldelser af Ingredienserne',
    'Der Stoffwechsel spielt eine zentrale Rolle bei der Gewichtsreduktion. Viele Anwender berichten von Schwierigkeiten, auf natürliche Weise abspecken zu können. Hier kommt die <strong>Slimanol</strong> Formel mit ihrer fortschrittlichen <strong>Zusammensetzung</strong> ins Spiel. Dieses pflanzliche Nahrungsergänzungsmittel zielt darauf ab, den Blutzuckerspiegels zu regulieren und Heißhungerattacken zu minimieren. In umfassenden Analysen und einem detaillierten <strong>Slimanol im Test</strong> untersuchen wir, wie effizient dieses Produkt wirklich ist.': 'Stofskiftet spiller en central rolle i vægttab. Mange brugere rapporterer om vanskeligheder ved at tabe sig naturligt. Her kommer <strong>Slimanol</strong> formlen med dens avancerede <strong>sammensætning</strong> ind i billedet. Dette plantebaserede kosttilskud sigter mod at regulere blodsukkerniveauet og minimere cravings. I omfattende analyser i <strong>Slimanol test</strong> undersøger vi, hvor effektivt dette produkt i virkeligheden er.',

    'Wirkung von Slimanol und Vorteile von Slimanol': 'Virkning og Fordele ved Slimanol',
    'Die <strong>Wirkung der Kapseln</strong> beruht auf einer gut verträglichen Mischung. Das Herzstück der <strong>Slimanol Inhaltsstoffe</strong> bildet die <strong>liposomale</strong> Technologie, wodurch die Bioverfügbarkeit maximiert wird. <strong>Grüner Tee-Extrakt (EGCG)</strong>, beruhigende <strong>Mariendistel</strong> (bzw. Mariendistel-Extrakt) und wertvolles <strong>Chrom</strong> unterstützen gemeinsam eine ausgewogene Ernährung. Ein weiterer essentieller Wirkstoff ist der <strong>Berberis aristata-Extrakt (Berberin)</strong>. Durch diese <strong>Inhaltsstoffe von Slimanol</strong> berichten Anwender von einer effektive Unterstützung beim Abnehmen und gesteigerter Energie. Viele Anwender betonen, <strong>dass Slimanol</strong> regelmäßig eingenommen, einen spürbaren <strong>Effekt</strong> auf die Fettverbrennung hat.': '<strong>Kapslernes virkning</strong> er baseret på en veltolereret blanding. Hjertet i <strong>Slimanol ingredienserne</strong> er den <strong>liposomale</strong> teknologi, som maksimerer biotilgængeligheden. <strong>Grøn te-ekstrakt (EGCG)</strong>, beroligende <strong>marietidsel</strong> og værdifuld <strong>krom</strong> understøtter sammen en afbalanceret kost. En anden vigtig aktiv ingrediens er <strong>Berberis aristata-ekstrakt (Berberin)</strong>. Gennem disse <strong>Slimanol ingredienser</strong> rapporterer brugere om effektiv støtte til vægttab og øget energi. Mange brugere understreger, at når <strong>Slimanol tages regelmæssigt</strong>, har det en mærkbar <strong>effekt</strong> på fedtforbrændingen.',

    'Slimanol Einnahme, Dosierung und Verträglichkeit': 'Slimanol Indtagelse, Dosering og Tolerance',
    'Die <strong>Einnahme von Slimanol</strong> ist unkompliziert. Die empfohlene <strong>Slimanol Dosierung</strong> umfasst die regelmäßige <strong>Einnahme der Kapseln</strong> vor den Mahlzeiten (Slimanol Einnahme). Jede Dose enthält <strong>60 Kapseln</strong>, was bei der empfohlen Anwendung genau für einen Monatsbedarf reicht. Wenn Sie <strong>Slimanol regelmäßig</strong> nehmen, wird empfohlen, dies stets in Kombination mit ausgewogene Ernährung und regelmäßiger Bewegung zu tun, um den Stoffwechsel optimal zu stärken.': '<strong>Indtagelsen af Slimanol</strong> er ukompliceret. Den anbefalede <strong>Slimanol dosering</strong> inkluderer regelmæssig <strong>indtagelse af kapslerne</strong> før måltider. Hver bøtte indeholder <strong>60 kapsler</strong>, hvilket rækker præcis til en måneds forbrug med den anbefalede anvendelse. Når du <strong>tager Slimanol regelmæssigt</strong>, anbefales det altid at gøre dette i kombination med en afbalanceret kost og regelmæssig motion for at styrke stofskiftet optimalt.',

    'Gibt es Nebenwirkungen oder Risiken bei Slimanol Kapseln?': 'Er der Bivirkninger eller Risici ved Slimanol Kapsler?',
    'Eine entscheidende Frage bei jedem Nahrungsergänzungsmittel wie Slimanol betrifft mögliche <strong>Slimanol Nebenwirkungen</strong> oder Risiken. Aufgrund seiner <strong>pflanzlichen Zusammensetzung</strong> und der Fokus auf natürliche Inhaltsstoffe wird das Produkt generell hinsichtlich der <strong>Verträglichkeit</strong> als sehr gut eingestuft. Irgendeine schwerwiegende <strong>Nebenwirkung</strong> wurde selten dokumentiert. Es richtet sich an Erwachsene; für Jugendliche unter <strong>18 Jahren</strong> ist das Produkt nicht vorgesehen. Personen mit bekannten Allergien gegen einen der Inhaltsstoffe sollten vor der Einnahme Rücksprache mit einem Arzt halten. Bewahren Sie das Produkt stets außerhalb der Reichweite von Kindern auf.': 'Et afgørende spørgsmål med ethvert kosttilskud som Slimanol vedrører mulige <strong>bivirkninger</strong> eller risici. På grund af dets <strong>plantebaserede sammensætning</strong> og fokus på naturlige ingredienser, er produktet generelt vurderet som meget godt med hensyn til <strong>tolerance</strong>. Eventuelle alvorlige <strong>bivirkninger</strong> er sjældent dokumenteret. Det henvender sig til voksne; produktet er ikke beregnet til teenagere under <strong>18 år</strong>. Personer med kendte allergier bør konsultere en læge inden brug. Opbevar altid produktet utilgængeligt for børn.',

    'Slimanol Erfahrungen und Bewertungen der Anwender (Slimanol Stiftung Warentest)': 'Slimanol Erfaringer og Brugeranmeldelser',
    'Die <strong>Slimanol Bewertung</strong> in der Praxis spricht Bände: Zahlreiche <strong>Slimanol Erfahrungen und Bewertungen</strong> untermauern die <strong>Wirksamkeit von Slimanol</strong>. Ob im unabhängigen <strong>Slimanol Test</strong> oder beim Vergleich mit anderen Diät-Präparaten, die <strong>Erfahrungen und Bewertungen</strong> der Käufer heben meist die einfache Anwendung und die positiven Auswirkungen während der Diät hervor. Oftmals wird fälschlicherweise nach einem <strong>Slimanol Stiftung Warentest</strong> gesucht. Fakt ist, dass die hohe Zufriedenheit vieler Käufer – insbesondere beim Thema „Slimanol jetzt seit mehreren Wochen ausprobiert“ – die starke <strong>Slimanol Wirkung</strong> und Verträglichkeit bestätigt. Die echte <strong>Slimanol Eigenschaften</strong> kommen nach einiger Zeit zum Vorschein.': '<strong>Slimanol anmeldelser</strong> i praksis taler for sig selv: Mange <strong>Slimanol erfaringer og anmeldelser</strong> underbygger <strong>Slimanols effektivitet</strong>. Uanset om det er i en <strong>Slimanol test</strong> eller i sammenligning med andre præparater, fremhæver købernes <strong>erfaringer og anmeldelser</strong> generelt den enkle brug og de positive virkninger. Mange købere er ekstremt tilfredse, hvilket bekræfter produktets stærke <strong>virkning</strong> og sikkerhed. De sande fordele kommer frem over tid.',

    'Wo kann man Slimanol kaufen zum besten Preis?': 'Hvor kan man købe Slimanol til den bedste pris?',
    'Wenn Sie <strong>Slimanol kaufen</strong> möchten, achten Sie immer darauf, das Originalprodukt zu ergattern. Ein fairer Slimanol Preis in Kombination mit bester Qualität ist entscheidend für Ihre Erfolgsgeschichte. Die optimale Slimanol Anwendung entfaltet sich nur mit der originalen <strong>Kapsel</strong>. Informieren Sie sich im Bereich "Häufig gestellte Fragen" weiter oben auf dieser Seite, um tiefer in die Details einzutauchen.': 'Hvis du vil <strong>købe Slimanol</strong>, skal du altid sørge for at få det originale produkt. En fair Slimanol-pris i kombination med den bedste kvalitet er afgørende for din succeshistorie. Den optimale indvirkning udfolder sig kun med den originale <strong>kapsel</strong>. Find mere information i "Ofte Stillede Spørgsmål" længere oppe for at dykke ned i detaljerne.',

    '>Kontakt<': '>Kontakt<',
    '>AGB<': '>Vilkår og Betingelser<',
    '>Datenschutzrichtlinie<': '>Privatlivspolitik<',
    '>Rückgabe<': '>Returnering<',

    'Die Aussagen auf dieser Website wurden nicht von einer Aufsichtsbehörde bewertet. Dieses Produkt ist nicht zur Diagnose, Behandlung, Heilung oder Vorbeugung von Krankheiten bestimmt.': 'Udtalelserne på dette websted er ikke blevet evalueret af nogen regulerende myndighed. Dette produkt er ikke beregnet til at diagnosticere, behandle, helbrede eller forebygge nogen sygdom.',
    'Die auf dieser Website angebotenen Inhalte und Produkte basieren auf der Meinung des Autors und werden wie besehen und nach Verfügbarkeit zur Verfügung gestellt. Konsultieren Sie immer einen Arzt, bevor Sie eine neue Diät, ein neues Nahrungsergänzungsmittel oder ein neues Trainingsprogramm beginnen.': 'Indholdet og produkterne, der tilbydes på dette websted, er baseret på forfatterens mening og leveres "som de er" og "efter tilgængelighed". Konsulter altid en sundhedsprofessionel, før du starter en ny diæt, et nyt kosttilskud eller et nyt træningsprogram.',
    'WICHTIGER HINWEIS: Wir sind ein unabhängiger Distributor (Werbepartner) und NICHT der Hersteller dieses Produkts. Alle Verkäufe werden sicher durch den offiziellen Hersteller abgewickelt. Wir erhalten eine Provision für Käufe, die über die Links auf dieser Website getätigt werden.': 'VIGTIG MEDDELELSE: Vi er en uafhængig distributør (reklamepartner) og IKKE producenten af dette produkt. Alle salg behandles sikkert af den officielle producent. Vi modtager en kommission for køb foretaget gennem linkene på dette websted.',
    'Alle Rechte vorbehalten.': 'Alle rettigheder forbeholdes.',

    'Kontakt & Support': 'Kontakt & Support',
    '<strong>Hinweis:</strong> Wir agieren als unabhängiger Werbe- und Vertriebspartner für Slimanol.': '<strong>Bemærk:</strong> Vi fungerer som en uafhængig reklame- og distributionspartner for Slimanol.',
    'Bei Fragen zu Ihrer Bestellung, dem Versand oder der 60-Tage-Garantie, beziehen Sie sich bitte auf die Kontaktinformationen, die auf der sicheren Zahlungsseite des Herstellers angegeben sind, nachdem Sie Ihr Land ausgewählt haben.': 'For spørgsmål om din ordre, forsendelse eller 60-dages garantien, henvises der til kontaktoplysningerne på producentens sikre betalingsside, efter du har valgt dit land.',
    'Alle Verkäufe, Logistik und Kundensupport werden direkt vom offiziellen Anbieter abgewickelt, um Sicherheit und Geschwindigkeit zu gewährleisten.': 'Alle salg, logistik og kundesupport håndteres direkte af den officielle leverandør for at sikre sikkerhed og hastighed.',

    'Allgemeine Geschäftsbedingungen': 'Generelle Vilkår og Betingelser',
    '1. Allgemeine Geschäftsbedingungen': '1. Generelle Vilkår og Betingelser',
    'Diese Website fungiert als Werbekanal und Vermittler. Wenn Sie auf Links zum Kauf klicken, stimmen Sie zu, zum sicheren Zahlungs-Gateway des Herstellers weitergeleitet zu werden.': 'Denne hjemmeside fungerer som en reklamekanal og formidler. Ved at klikke på links for at købe, accepterer du at blive omdirigeret til producentens sikre betalingsgateway.',
    '2. Produktnutzung': '2. Produktanvendelse',
    'Slimanol ist ein Nahrungsergänzungsmittel. Es ist nicht zur Diagnose, Behandlung, Heilung oder Vorbeugung von Krankheiten bestimmt. Konsultieren Sie vor der Anwendung immer einen Gesundheitsdienstleister.': 'Slimanol er et kosttilskud. Det er ikke beregnet til at diagnosticere, behandle, helbrede eller forebygge nogen sygdom. Konsulter altid en sundhedsudbyder før brug.',
    '3. Käufe': '3. Køb',
    'Wir verarbeiten keine Zahlungen und versenden keine Artikel lokal. Alle Transaktionen werden sicher von den offiziellen Vertriebszentren des Herstellers abgewickelt.': 'Vi behandler ikke betalinger eller sender varer lokalt. Alle transaktioner håndteres sikkert af producentens officielle distributionscentre.',

    'Datenschutzrichtlinie (DSGVO)': 'Privatlivspolitik (GDPR)',
    '1. Datenerfassung': '1. Dataindsamling',
    'In Übereinstimmung mit der DSGVO erfassen wir Standard-Traffic-Daten (Cookies, IP-Adresse) über anerkannte Tracking-Technologien für das Click-Routing bei der Nutzung dieser Zielseite.': 'I overensstemmelse med GDPR indsamler vi standard trafikdata (cookies, IP-adresse) via anerkendte sporingsteknologier til klikrouting, når du bruger denne landingsside.',
    '2. Nutzung': '2. Anvendelse',
    'Wir erfassen auf dieser Domain KEINE Zahlungsinformationen oder hochsensiblen personenbezogenen Daten. Ihre Daten werden ausschließlich verwendet, um Sie zum richtigen regionalen Anbieter weiterzuleiten.': 'Vi indsamler IKKE betalingsoplysninger eller meget følsomme personoplysninger på dette domæne. Dine data bruges udelukkende til at dirigere dig til den rigtige regionale udbyder.',
    '3. Sicherheit': '3. Sikkerhed',
    'Alle Transaktionen und die Erfassung sensibler Daten erfolgen auf den SSL-verschlüsselten, PCI-konformen Zahlungs-Gateways des Herstellers.': 'Alle transaktioner og indsamling af følsomme data sker på producentens SSL-krypterede, PCI-kompatible betalingsgateways.',

    'Rückgaberichtlinien & 60-Tage-Garantie': 'Returpolitik & 60-Dages Garanti',
    '<strong>60-Tage Geld-zurück-Garantie:</strong> Der Hersteller steht zu 100% hinter Slimanol. Wenn Sie Slimanol wie angegeben verwenden und innerhalb von 60 Tagen nach dem Kauf nicht vollständig mit Ihren Ergebnissen zufrieden sind, haben Sie gemäß den Bedingungen des Herstellers Anspruch auf eine Rückerstattung.': '<strong>60-Dages Tilfredshedsgaranti:</strong> Producenten står 100% bag Slimanol. Hvis du bruger Slimanol som anvist og ikke er fuldt tilfreds med dine resultater inden for 60 dage efter køb, er du berettiget til refusion i henhold til producentens betingelser.',
    '<strong>Rückgabeprozess:</strong> Um eine Rückgabe einzuleiten, verwenden Sie bitte die Kontakt-E-Mail oder Telefonnummer, die in Ihrer Bestellbestätigungs-E-Mail vom offiziellen Anbieter angegeben ist.': '<strong>Returproces:</strong> For at starte en returnering, bedes du benytte den kontakt-e-mail eller det telefonnummer, der er angivet i din ordrebekræftelses-e-mail fra den officielle udbyder.',
    '<strong>Beschädigte Artikel:</strong> Wenn Ihre Bestellung beschädigt ankommt, melden Sie dies bitte sofort dem Support-Team des tatsächlichen Anbieters, um einen Ersatz zu erhalten.': '<strong>Beskadigede varer:</strong> Hvis din ordre ankommer beskadiget, bedes du straks rapportere det til den faktiske udbyders supportteam for at få en erstatning.',
    'JETZT BESTELLEN – 60-Tage Garantie': 'BESTIL NU - 60-Dages Garanti'
}

for ger, da in replacements.items():
    html = html.replace(ger, da)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Translation to Danish complete')
