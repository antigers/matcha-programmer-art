import json
import shutil
import zipfile
from pathlib import Path

MATCHA_PATH = Path('./matcha-flavoured/')
MATCHA_ASSETS = MATCHA_PATH / 'MF_resourcepack' / 'assets'
MATCHA_PROGRAMMER_ART_ASSETS = Path('assets')
OUTPUT_ASSETS = Path('./output/assets/')
OUTPUT_ASSETS.mkdir(parents=True, exist_ok=True)

PATHS_TO_COPY_FROM_MATCHA = (
    # basic stuff
    'matcha',
    'minecraft/atlases',
    'minecraft/font',
    'minecraft/lang',
    'minecraft/particles',
    'minecraft/sounds',
    'minecraft/texts',
    'minecraft/sounds.json',
    'minecraft/textures/environment/celestial',
    'minecraft/textures/font',
    'minecraft/textures/gui/title',
    'minecraft/textures/misc',

    # Blockstates
    'minecraft/blockstates/bedrock_buster.json',
    'minecraft/blockstates/petrified_oak_slab.json',
    'minecraft/blockstates/target.json',
    'minecraft/blockstates/warding_stone.json',

    # Overridden block textures
    'minecraft/textures/block/emerald_block.png',  # Block of Obol
    'minecraft/textures/block/redstone_ore.png',  # Sulfurous Quartz Deposit
    'minecraft/textures/block/deepslate_redstone_ore.png',  # Sulfur Deposit
    'minecraft/textures/block/target_side.png',  # Copper Eye
    'minecraft/textures/block/target_side_on.png',  # Copper Eye
    'minecraft/textures/block/target_top.png',  # Copper Eye
    'minecraft/textures/block/target_top_on.png',  # Copper Eye
    'minecraft/textures/block/netherite_block.png',  # Block of Adamant

    # Block models
    'minecraft/models/block/target.json',  # Copper Eye
    'minecraft/models/block/target_on.json',  # Copper Eye
    'minecraft/models/block/petrified_oak_slab.json',  # Dirt Slab
    'minecraft/models/block/petrified_oak_slab_1.json',  # Dirt Slab
    'minecraft/models/block/petrified_oak_slab_2.json',  # Dirt Slab
    'minecraft/models/block/petrified_oak_slab_3.json',  # Dirt Slab
    'minecraft/models/block/petrified_oak_slab_top.json',  # Dirt Slab
    'minecraft/models/block/petrified_oak_slab_top_1.json',  # Dirt Slab
    'minecraft/models/block/petrified_oak_slab_top_2.json',  # Dirt Slab
    'minecraft/models/block/petrified_oak_slab_top_3.json',  # Dirt Slab

    # Overridden item textures
    'minecraft/textures/item/beetroot.png',  # Tomatoes
    'minecraft/textures/item/beetroot_seeds.png',  # Tomato Seeds
    'minecraft/textures/item/beetroot_soup.png',  # Milk Bottle
    'minecraft/textures/item/blaze_powder.png',  # Raw Estus
    'minecraft/textures/item/blaze_rod.png',  # Stabilized Estus
    'minecraft/textures/item/cookie.png',  # Cheese
    'minecraft/textures/item/emerald.png',  # Obol
    'minecraft/textures/item/ender_eye.png',  # Eye of Ender
    'minecraft/textures/item/ender_pearl.png',  # Stable Void
    'minecraft/textures/item/gunpowder.png',  # Sulfur Chunk
    'minecraft/textures/item/netherite_upgrade_smithing_template.png',  # Smithing Upgrade Template
    'minecraft/textures/item/nether_star.png',  # Divine Favor
    'minecraft/textures/item/prismarine_shard.png',  # Raw Silver
    'minecraft/textures/item/rabbit_hide.png',  # Tattered Leather
    'minecraft/textures/item/redstone.png',  # Electric Wire
    'minecraft/textures/item/suspicious_stew.png',  # Compat with clay bowl
    'minecraft/textures/item/turtle_scute.png',  # Divine Fragment

    # Item models
    'minecraft/models/item/blaze_spawn_egg.json',  # Nazar
    'minecraft/models/item/breeze_rod.json',  # Baked Pumpkin
    'minecraft/models/item/enderman_spawn_egg.json',  # flour
    'minecraft/models/item/endermite_spawn_egg.json',  # benzene
    'minecraft/models/item/fermented_spider_eye.json',  # baked_apple
    'minecraft/models/item/ghast_spawn_egg.json',  # uncooked_pumpkin_curry
    'minecraft/models/item/glistering_melon_slice.json',  # baked_golden_apple
    'minecraft/models/item/happy_ghast_spawn_egg.json',  # oil
    'minecraft/models/item/hoglin_spawn_egg.json',  # seitan
    'minecraft/models/item/magma_cream.json',  # sweet_berry_mash
    'minecraft/models/item/magma_cube_spawn_egg.json',  # flour_bag
    'minecraft/models/item/mushroom_stew.json',  # chocolate
    'minecraft/models/item/piglin_brute_spawn_egg.json',  # carbon_rich_iron
    'minecraft/models/item/piglin_spawn_egg.json',  # molasses
    'minecraft/models/item/rabbit_foot.json',  # braised_brown_mushroom
    'minecraft/models/item/resin_brick.json',  # Silver Alloy
    'minecraft/models/item/rotten_flesh.json',  # Glow Mash
    'minecraft/models/item/shulker_spawn_egg.json',  # dough
    'minecraft/models/item/strider_spawn_egg.json',  # uncooked_curry
    'minecraft/models/item/vindicator_spawn_egg.json',  # raw_diamond
    'minecraft/models/item/wither_skeleton_spawn_egg.json',  # uncooked_ramen
    'minecraft/models/item/zoglin_spawn_egg.json',  # uncooked_paneer_makhani
    'minecraft/models/item/zombified_piglin_spawn_egg.json',  # uncooked_green_curry

    # Armor Trims support
    'minecraft/models/item/chainmail_boots_electrum_trim.json',
    'minecraft/models/item/chainmail_boots_hepatizon_trim.json',
    'minecraft/models/item/chainmail_boots_shakudo_trim.json',
    'minecraft/models/item/chainmail_chestplate_electrum_trim.json',
    'minecraft/models/item/chainmail_chestplate_hepatizon_trim.json',
    'minecraft/models/item/chainmail_chestplate_shakudo_trim.json',
    'minecraft/models/item/chainmail_helmet_electrum_trim.json',
    'minecraft/models/item/chainmail_helmet_hepatizon_trim.json',
    'minecraft/models/item/chainmail_helmet_shakudo_trim.json',
    'minecraft/models/item/chainmail_leggings_electrum_trim.json',
    'minecraft/models/item/chainmail_leggings_hepatizon_trim.json',
    'minecraft/models/item/chainmail_leggings_shakudo_trim.json',
    'minecraft/models/item/copper_boots_electrum_trim.json',
    'minecraft/models/item/copper_boots_hepatizon_trim.json',
    'minecraft/models/item/copper_boots_shakudo_trim.json',
    'minecraft/models/item/copper_chestplate_electrum_trim.json',
    'minecraft/models/item/copper_chestplate_hepatizon_trim.json',
    'minecraft/models/item/copper_chestplate_shakudo_trim.json',
    'minecraft/models/item/copper_helmet_electrum_trim.json',
    'minecraft/models/item/copper_helmet_hepatizon_trim.json',
    'minecraft/models/item/copper_helmet_shakudo_trim.json',
    'minecraft/models/item/copper_leggings_electrum_trim.json',
    'minecraft/models/item/copper_leggings_hepatizon_trim.json',
    'minecraft/models/item/copper_leggings_shakudo_trim.json',
    'minecraft/models/item/diamond_boots_electrum_trim.json',
    'minecraft/models/item/diamond_boots_hepatizon_trim.json',
    'minecraft/models/item/diamond_boots_shakudo_trim.json',
    'minecraft/models/item/diamond_chestplate_electrum_trim.json',
    'minecraft/models/item/diamond_chestplate_hepatizon_trim.json',
    'minecraft/models/item/diamond_chestplate_shakudo_trim.json',
    'minecraft/models/item/diamond_helmet_electrum_trim.json',
    'minecraft/models/item/diamond_helmet_hepatizon_trim.json',
    'minecraft/models/item/diamond_helmet_shakudo_trim.json',
    'minecraft/models/item/diamond_leggings_electrum_trim.json',
    'minecraft/models/item/diamond_leggings_hepatizon_trim.json',
    'minecraft/models/item/diamond_leggings_shakudo_trim.json',
    'minecraft/models/item/golden_boots_electrum_trim.json',
    'minecraft/models/item/golden_boots_hepatizon_trim.json',
    'minecraft/models/item/golden_boots_shakudo_trim.json',
    'minecraft/models/item/golden_chestplate_electrum_trim.json',
    'minecraft/models/item/golden_chestplate_hepatizon_trim.json',
    'minecraft/models/item/golden_chestplate_shakudo_trim.json',
    'minecraft/models/item/golden_helmet_electrum_trim.json',
    'minecraft/models/item/golden_helmet_hepatizon_trim.json',
    'minecraft/models/item/golden_helmet_shakudo_trim.json',
    'minecraft/models/item/golden_leggings_electrum_trim.json',
    'minecraft/models/item/golden_leggings_hepatizon_trim.json',
    'minecraft/models/item/golden_leggings_shakudo_trim.json',
    'minecraft/models/item/iron_boots_electrum_trim.json',
    'minecraft/models/item/iron_boots_hepatizon_trim.json',
    'minecraft/models/item/iron_boots_shakudo_trim.json',
    'minecraft/models/item/iron_chestplate_electrum_trim.json',
    'minecraft/models/item/iron_chestplate_hepatizon_trim.json',
    'minecraft/models/item/iron_chestplate_shakudo_trim.json',
    'minecraft/models/item/iron_helmet_electrum_trim.json',
    'minecraft/models/item/iron_helmet_hepatizon_trim.json',
    'minecraft/models/item/iron_helmet_shakudo_trim.json',
    'minecraft/models/item/iron_leggings_electrum_trim.json',
    'minecraft/models/item/iron_leggings_hepatizon_trim.json',
    'minecraft/models/item/iron_leggings_shakudo_trim.json',
    'minecraft/models/item/netherite_boots_electrum_trim.json',
    'minecraft/models/item/netherite_boots_hepatizon_trim.json',
    'minecraft/models/item/netherite_boots_shakudo_trim.json',
    'minecraft/models/item/netherite_chestplate_electrum_trim.json',
    'minecraft/models/item/netherite_chestplate_hepatizon_trim.json',
    'minecraft/models/item/netherite_chestplate_shakudo_trim.json',
    'minecraft/models/item/netherite_helmet_electrum_trim.json',
    'minecraft/models/item/netherite_helmet_hepatizon_trim.json',
    'minecraft/models/item/netherite_helmet_shakudo_trim.json',
    'minecraft/models/item/netherite_leggings_electrum_trim.json',
    'minecraft/models/item/netherite_leggings_hepatizon_trim.json',
    'minecraft/models/item/netherite_leggings_shakudo_trim.json',
    'minecraft/models/item/turtle_helmet_electrum_trim.json',
    'minecraft/models/item/turtle_helmet_hepatizon_trim.json',
    'minecraft/models/item/turtle_helmet_shakudo_trim.json',
    'minecraft/items/chainmail_boots.json',
    'minecraft/items/chainmail_chestplate.json',
    'minecraft/items/chainmail_helmet.json',
    'minecraft/items/chainmail_leggings.json',
    'minecraft/items/copper_boots.json',
    'minecraft/items/copper_chestplate.json',
    'minecraft/items/copper_helmet.json',
    'minecraft/items/copper_leggings.json',
    'minecraft/items/diamond_boots.json',
    'minecraft/items/diamond_chestplate.json',
    'minecraft/items/diamond_helmet.json',
    'minecraft/items/diamond_leggings.json',
    'minecraft/items/golden_boots.json',
    'minecraft/items/golden_chestplate.json',
    'minecraft/items/golden_helmet.json',
    'minecraft/items/golden_leggings.json',
    'minecraft/items/iron_boots.json',
    'minecraft/items/iron_chestplate.json',
    'minecraft/items/iron_helmet.json',
    'minecraft/items/iron_leggings.json',
    'minecraft/items/leather_boots.json',
    'minecraft/items/leather_chestplate.json',
    'minecraft/items/leather_helmet.json',
    'minecraft/items/leather_leggings.json',
    'minecraft/items/netherite_boots.json',
    'minecraft/items/netherite_chestplate.json',
    'minecraft/items/netherite_helmet.json',
    'minecraft/items/netherite_leggings.json',
    'minecraft/items/turtle_helmet.json',
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
