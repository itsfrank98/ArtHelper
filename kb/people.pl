[cities].

:- multifile fact/2.
:- dynamic fact/2.

%DEFINITION OF SOME PEOPLE AND ARTISTS
fact(artist, (leonardo_da_vinci, 'Leonardo di ser Piero da Vinci', 1452, 1519)).
fact(artist, (michelangelo, 'Michelangelo di Lodovico Buonarroti Simoni', 1475, 1564)).
fact(artist, (filippo_brunelleschi, 'Filippo di ser Brunellesco Lapi', 1377, 1446)).
fact(artist, (emilio_de_fabris, 'Emilio De Fabris', 1807, 1883)).
fact(artist, (arnolfo_di_cambio, 'Arnolfo Di Cambio', 1245, 1308)).
fact(artist, (raffaello, 'Raffaello Sanzio', 1483, 1520)).
fact(artist, (sandro_botticelli, 'Alessandro di Mariano di Vanni Filipepi', 1445, 1510)).
fact(artist, (piero_della_francesca, 'Piero di Benedetto de\' Franceschi', 1412, 1492)).
fact(artist, (caravaggio, 'Michelangelo Merisi', 1571, 1610)).
fact(artist, (tiziano, 'Tiziano Vecellio', 1489, 1576)).
fact(artist, (paolo_uccello, 'Paolo di Dono', 1397, 1475)).
fact(artist, (vincent_van_gogh, 'Vincent Willem Van Gogh', 1853, 1890)).
fact(artist, (leon_battista_alberti, 'Leon Battista Alberti', 1404, 1472)).
fact(artist, (masaccio, 'Tommaso di Ser Giovanni di Simone', 1401, 1428)).
fact(artist, (gherardo_silvani, 'Gherardo Silvani', 1579, 1675)).
fact(artist, (antonio_manetti, 'Antonio Manetti', 1423, 1497)).
fact(artist, (neri_fioravante, 'Neri di Fioravante', 1320, 1374)).

fact(influenced_by, (leonardo_da_vinci, [piero_della_francesca, masaccio])).
fact(influenced_by, (michelangelo, [masaccio])).
fact(influenced_by, (raffaello, [paolo_uccello, michelangelo])).
fact(influenced_by, (sandro_botticelli, [masaccio])).
fact(influenced_by, (caravaggio, [tiziano])).
fact(influenced_by, (tiziano, [raffaello, michelangelo])).

fact(portrayable, (holy_mary, 'Holy Mary')).
fact(portrayable, (st_joseph, 'St. Joseph')).
fact(portrayable, (magi, 'Magi')).
fact(portrayable, (adam, 'Adam')).
fact(portrayable, (eve, 'Eve')).
fact(portrayable, (god, 'God')).
fact(portrayable, (moses, 'Moses')).
fact(portrayable, (zacharias, 'Zacharias')).
fact(portrayable, (john_baptist, 'John the Baptist')).
fact(portrayable, (jesus, 'Jesus Christ')).
fact(portrayable, (clori, 'Chloris')).
fact(portrayable, (flora, 'Flora')).
fact(portrayable, (zefiro, 'Zefiro')).
fact(portrayable, (venere, 'Venere')).
fact(portrayable, (mercurio, 'Mercurio')).
fact(portrayable, (arianna, 'Ariadne')).
fact(portrayable, (bacchus, 'Bacchus')).
fact(portrayable, (marte, 'Marte')).
fact(portrayable, (fauni, 'Fauni')).
fact(portrayable, (federico_montefeltro, 'Federico da Montefeltro')).
fact(portrayable, (battista_sforza, 'Battista Sforza')).
fact(portrayable, (lorenzo_medici, 'Lorenzo de\' Medici')).
fact(portrayable, (dante, 'Dante Alighieri')).
fact(portrayable, (lisa_gherardini, 'Lisa Gherardini')).
fact(portrayable, (francesco_dellarovere, 'Francesco Maria della Rovere')).
fact(portrayable, (plato, 'Plato')).
fact(portrayable, (aristotele, 'Aristotele')).
fact(portrayable, (socrates, 'Socrates')).
fact(portrayable, (senofonte, 'Senofonte')).
fact(portrayable, (zenone, 'Zenone di Cizio')).
fact(portrayable, (pitagora, 'Pytagoras')).
fact(portrayable, (plotino, 'Plotino')).
fact(portrayable, (diogene, 'Diogene')).
fact(portrayable, (euclid, 'Euclid')).
fact(portrayable, (fornarina, 'Margherita Luti')).
fact(portrayable, (niccolo_tolentino, 'Niccolò da Tolentino')).
fact(portrayable, (bernardino_carda, 'Bernardino della Carda')).
fact(portrayable, (michele_attendolo, 'Michele Attendolo')).
fact(portrayable, (cupid, 'Cupid')).
fact(portrayable, (grazie, 'Grazie')).
fact(portrayable, (st_stephen, 'St. Stephen')).
fact(portrayable, (st_laurence, 'St. Laurence')).
fact(portrayable, (st_paul, 'St. Paul')).
fact(portrayable, (st_thomas, 'St. Thomas')).
fact(portrayable, (st_peter, 'St. Peter')).
fact(portrayable, (st_andrew, 'St. Andrew')).