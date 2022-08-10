%DEFINITION OF SOME MUSEUMS AND MONUMENTS
:- multifile fact/2.
:- dynamic fact/2.

fact(museum, (louvre, 'Louvre', paris)).
fact(museum, (vatican_museums, 'Musei Vaticani', rome)).
fact(museum, (uffizi, 'Galleria degli Uffizi', florence)).
fact(museum, (vangogh_museum, 'Van Gogh museum', amsterdam)).
fact(museum, (national_gallery, 'London national gallery', london)).
fact(museum, (pitti, 'Palazzo Pitti', florence)).
fact(museum, (borghese, 'Galleria borghese', rome)).
fact(museum, (sistine_chapel, 'Cappella Sistina', rome)).
fact(museum, (vatican_rooms, 'Stanze vaticane', rome)).

fact(church, (santa_maria_del_fiore, 'Santa Maria del Fiore', florence, 1296, 1903)).
fact(church, (santa_maria_novella, 'Santa Maria Novella', florence, 1279, 1360)).
fact(church, (santa_croce, 'Basilica di Santa Croce', florence, 1294, 1385)).
fact(church, (st_stephen, 'Église Saint-Étienne', caen, 1065, 1400)).
fact(church, (san_frediano, 'Chiesa di San Frediano in Cestello', florence, 1450, 1689)).
fact(church, (santo_spirito, 'Basilica di Santo Spirito', florence, 1444, 1487)).
fact(church, (orsanmichele, 'Chiesa di Orsanmichele', florence, 1337, 1380)).

fact(owns, (uffizi, [raffaello_selfportrait, san_romano_uffizi, della_rovere_portrait, venere_birth, primavera, tondo_doni, magi_adoration, federico_montefeltro_portrait, battista_sforza_portrait, spring, madonna_cardellino, magi_botticelli, madonna_casini])).
fact(owns, (pitti, [velata])).
fact(owns, (borghese, [bacco])).
fact(owns, (sistine_chapel, [adam_creation, universal_judice, eve_creation])).
fact(owns, (louvre, [monna_lisa, san_romano_louvre, madonna_piot])).
fact(owns, (national_gallery, [sunflowers, venere_marte, madonna_garofani, bacco_arianna, san_romano_nationalgallery])).
fact(owns, (vangogh_museum, [van_gogh_with_hat, van_gogh_while_painting, potato_eaters])).
fact(owns, (vatican_rooms, [athens_school, sacrament_dispute])).
fact(owns, (santa_maria_novella, [adam_animals_creation, eve_and_sin, holy_trinity])).

fact(designed, (santa_maria_del_fiore, [arnolfo_di_cambio, emilio_de_fabris, filippo_brunelleschi])).
fact(designed, (santa_croce, [arnolfo_di_cambio])).
fact(designed, (santa_maria_novella, [filippo_brunelleschi, leon_battista_alberti])).
fact(designed, (san_frediano, [gherardo_silvani])).
fact(designed, (santo_spirito, [filippo_brunelleschi, antonio_manetti])).
fact(designed, (orsanmichele, [neri_fioravante])).
fact(designed, (st_stephen, [])).