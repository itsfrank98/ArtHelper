% DEFINITION OF SOME STYLES. A style is a style that can be found in both artworks and architecture. An artistic style is a style that is applied only in paintings
:- multifile fact/2.
:- dynamic fact/2.

fact(style, (romanic, 'Romanic', 1000, 1200, architecture)).
fact(style, (gothic, 'Gothic', 1144, 1600, architecture)).
fact(style, (neogothic, 'Neogothic', 1790, 1900, architecture)).
fact(style, (baroque, 'Baroque', 1600, 1690, both)).
fact(style, (proto_renaissance, 'Proto Renaissance', 1200, 1400, both)).
fact(style, (early_renaissance, 'Early Renaissance', 1400, 1490, both)).
fact(style, (high_renaissance, 'High Renaissance', 1490, 1530, both)).
fact(style, (mannerism, 'Mannerism', 1492, 1580, art)).
fact(style, (neoclassicism, 'Neoclassicism', 1750, 1820, both)).
fact(style, (realism, 'Realism', 1840, 1880, artistic)).
fact(style, (impressionism, 'Impressionism', 1865, 1900, artistic)).
fact(style, (post_impressionism, 'Post Impressionism', 1886, 1905, artistic)).

fact(same_main_current, ([proto_renaissance, early_renaissance, high_renaissance])).
fact(same_main_current, ([gothic, neogothic])).
fact(same_main_current, ([impressionism, post_impressionism])).

fact(follows, (monna_lisa, [high_renaissance])). 
fact(follows, (magi_adoration, [early_renaissance])).
fact(follows, (magi_botticelli, [early_renaissance])).
fact(follows, (tondo_doni, [high_renaissance])).
fact(follows, (athens_school, [high_renaissance])). 
fact(follows, (raffaello_selfportrait, [high_renaissance])).
fact(follows, (velata, [high_renaissance])).
fact(follows, (madonna_cardellino, [high_renaissance])).
fact(follows, (madonna_garofani, [high_renaissance])).
fact(follows, (san_romano_uffizi, [early_renaissance])).
fact(follows, (san_romano_louvre, [early_renaissance])).
fact(follows, (san_romano_nationalgallery, [early_renaissance])).
fact(follows, (adam_animals_creation, [early_renaissance])).
fact(follows, (eve_and_sin, [early_renaissance])).
fact(follows, (della_rovere_portrait, [high_renaissance])). 
fact(follows, (bacco_arianna, [high_renaissance])).
fact(follows, (venere_birth, [early_renaissance])).
fact(follows, (primavera, [early_renaissance])).
fact(follows, (venere_marte, [early_renaissance])).
fact(follows, (federico_montefeltro_portrait, [early_renaissance])).
fact(follows, (battista_sforza_portrait, [early_renaissance])).
fact(follows, (bacco, [baroque])).
fact(follows, (sunflowers, [post_impressionism])).
fact(follows, (van_gogh_with_hat, [post_impressionism])). 
fact(follows, (van_gogh_while_painting, [post_impressionism])).
fact(follows, (potato_eaters, [realism])).
fact(follows, (adam_creation, [high_renaissance])).
fact(follows, (eve_creation, [high_renaissance])).
fact(follows, (sacrament_dispute, [high_renaissance])).
fact(follows, (universal_judice, [mannerism])).
fact(follows, (holy_trinity, [early_renaissance])).
fact(follows, (madonna_casini, [early_renaissance])).

fact(follows, (santa_maria_del_fiore, [gothic, neogothic])).
fact(follows, (santa_maria_novella, [early_renaissance, gothic])).
fact(follows, (santa_croce, [high_renaissance, gothic, neogothic])).
fact(follows, (st_stephen, [romanic, gothic])).
fact(follows, (san_frediano, [baroque])).
fact(follows, (santo_spirito, [early_renaissance])).
fact(follows, (orsanmichele, [gothic])).