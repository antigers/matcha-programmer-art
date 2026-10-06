import json
import shutil
import zipfile
from pathlib import Path

MATCHA_PATH = Path('./matcha-flavoured/')
MATCHA_ASSETS = MATCHA_PATH / 'MF_resourcepack' / 'assets'
MATCHA_PROGRAMMER_ART_ASSETS = Path('assets')
OUTPUT_ASSETS = Path('./output/assets/')
OUTPUT_ASSETS.mkdir(parents=True, exist_ok=True)

shutil.unpack_archive('./Matcha Vanilla Flavoured.zip', './output')

PATHS_TO_REMOVE_FROM_VANILLA_FLAVOURED = (
    'axiom',
    'iteminteractions',
    'jbt',
    'minecraft/lang',
    '../pack.png',
    '../pack.mcmeta',

    # Unneeded models
    'minecraft/models/block/orientable_furnace.json',
    'minecraft/models/block/orientable_vertical_with_bottom.json',
    'minecraft/models/block/orientable_with_all_sides.json',
    'minecraft/models/block/dropper.json',
    'minecraft/models/block/dropper_vertical.json',
    'minecraft/models/block/dispenser.json',
    'minecraft/models/block/dispenser_vertical.json',

    # Unneeded item textures
    'minecraft/textures/item/armadillo_spawn_egg.png',
    'minecraft/textures/item/benzene.png',
    'minecraft/textures/item/cooked_cod.png',
    'minecraft/textures/item/cooked_salmon.png',
    'minecraft/textures/item/disc_fragment_5.png',
    'minecraft/textures/item/echo_fish.png',
    'minecraft/textures/item/echo_shard.png',
    'minecraft/textures/item/echo_shard.png.mcmeta',
    'minecraft/textures/item/echo_shard_alt.png',
    'minecraft/textures/item/frog_spawn_egg.png',
    'minecraft/textures/item/multishot.png',
    'minecraft/textures/item/music_disc_5.png',
    'minecraft/textures/item/music_disc_11.png',
    'minecraft/textures/item/music_disc_13.png',
    'minecraft/textures/item/music_disc_blocks.png',
    'minecraft/textures/item/music_disc_bounce.png',
    'minecraft/textures/item/music_disc_cat.png',
    'minecraft/textures/item/music_disc_chirp.png',
    'minecraft/textures/item/music_disc_creator.png',
    'minecraft/textures/item/music_disc_creator_music_box.png',
    'minecraft/textures/item/music_disc_far.png',
    'minecraft/textures/item/music_disc_lava_chicken.png',
    'minecraft/textures/item/music_disc_mall.png',
    'minecraft/textures/item/music_disc_mellohi.png',
    'minecraft/textures/item/music_disc_otherside.png',
    'minecraft/textures/item/music_disc_pigstep.png',
    'minecraft/textures/item/music_disc_precipice.png',
    'minecraft/textures/item/music_disc_relic.png',
    'minecraft/textures/item/music_disc_stal.png',
    'minecraft/textures/item/music_disc_strad.png',
    'minecraft/textures/item/music_disc_tears.png',
    'minecraft/textures/item/music_disc_wait.png',
    'minecraft/textures/item/music_disc_ward.png',
    'minecraft/textures/item/nether_wart.png',
    'minecraft/textures/item/puerquito.png',
    'minecraft/textures/item/tadpole_spawn_egg.png',

    # Unneeded block textures
    'minecraft/textures/block/campfire_log.png',
    'minecraft/textures/block/campfire_log_lit.png',
    'minecraft/textures/block/campfire_log_lit.png.mcmeta',
    'minecraft/textures/block/deepslate_emerald_ore.png',
    'minecraft/textures/block/deepslate_emerald_ore.png.mcmeta',
    'minecraft/textures/block/deepslate_lapis_ore.png',
    'minecraft/textures/block/dispenser_back.png',
    'minecraft/textures/block/dispenser_bottom.png',
    'minecraft/textures/block/dispenser_bottom_vertical.png',
    'minecraft/textures/block/dispenser_east.png',
    'minecraft/textures/block/dispenser_side_vertical.png',
    'minecraft/textures/block/dispenser_top.png',
    'minecraft/textures/block/dispenser_west.png',
    'minecraft/textures/block/dropper_back.png',
    'minecraft/textures/block/dropper_bottom.png',
    'minecraft/textures/block/dropper_bottom_vertical.png',
    'minecraft/textures/block/dropper_top.png',
    'minecraft/textures/block/dropper_west.png',
    'minecraft/textures/block/dropper_east.png',
    'minecraft/textures/block/dropper_side_vertical.png',
    'minecraft/textures/block/furnace_front_off.png',
    'minecraft/textures/block/furnace_front_on.png',
    'minecraft/textures/block/furnace_front_on_1.png',
    'minecraft/textures/block/furnace_front_on_1.png.mcmeta',
    'minecraft/textures/block/furnace_side.png',
    'minecraft/textures/block/furnace_top.png',
    'minecraft/textures/block/furnace_top_1.png',
    'minecraft/textures/block/furnace_top_1.png.mcmeta',
    'minecraft/textures/block/lapis_ore.png',
    'minecraft/textures/block/nether_quartz_ore.png',
    'minecraft/textures/block/smoker_bottom.png',
    'minecraft/textures/block/smoker_front.png',
    'minecraft/textures/block/smoker_front_on.png',
    'minecraft/textures/block/smoker_front_on.png.mcmeta',
    'minecraft/textures/block/smoker_side.png',
    'minecraft/textures/block/smoker_top.png',
    'minecraft/textures/block/emerald_ore.png',
    'minecraft/textures/block/emerald_ore.png.mcmeta',

    'minecraft/textures/entity/equipment',

    'matcha/sounds/custom/malachiteORG.ogg'
)

for path_str in PATHS_TO_REMOVE_FROM_VANILLA_FLAVOURED:
    path = OUTPUT_ASSETS / path_str
    if path.is_file():
        path.unlink()
    else:
        shutil.rmtree(path)


PATHS_TO_COPY_FROM_MATCHA = (
    'minecraft/lang',
    'minecraft/textures/environment/celestial',
    'minecraft/textures/misc',
    'minecraft/textures/item/emerald.png',
    'minecraft/textures/item/rabbit_hide.png',
    'minecraft/textures/item/suspicious_stew.png',
    'minecraft/textures/block/emerald_block.png',
)

for path_str in PATHS_TO_COPY_FROM_MATCHA:
    path = MATCHA_ASSETS / path_str
    if path.is_file():
        (OUTPUT_ASSETS / path_str).parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(path, OUTPUT_ASSETS / path_str)
    else:
        shutil.copytree(path, OUTPUT_ASSETS / path_str, dirs_exist_ok=True)

shutil.copytree(MATCHA_PROGRAMMER_ART_ASSETS, OUTPUT_ASSETS, dirs_exist_ok=True)

JSON_PATHS_TO_MERGE = (
    'minecraft/lang/en_us.json',
    'minecraft/lang/ru_ru.json',
)

for path_str in JSON_PATHS_TO_MERGE:
    matcha_json = json.loads((MATCHA_ASSETS / path_str).read_text(encoding='utf-8'))
    programmer_json = json.loads((MATCHA_PROGRAMMER_ART_ASSETS / path_str).read_text(encoding='utf-8'))
    with open(OUTPUT_ASSETS / path_str, 'w') as file:
        file.write(json.dumps(matcha_json | programmer_json, ensure_ascii=False, indent=4))

shutil.make_archive('Matcha Programmer Art', format='zip', root_dir='output')
with zipfile.ZipFile('Matcha Programmer Art.zip', mode='a', compression=zipfile.ZIP_DEFLATED) as archive:
    for file in ('pack.mcmeta', 'pack.png', 'LICENSE'):
        archive.write(file)

shutil.rmtree('output')
