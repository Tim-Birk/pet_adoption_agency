"""Seed file to make sample data for pet_adoption db."""

from models import Pet, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If tables aren't empty, empty them
Pet.query.delete()

# Add pets
bixby = Pet(name='Bixby', species='dog', photo_url="https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/golden-retriever-royalty-free-image-506756303-1560962726.jpg?crop=0.672xw:1.00xh;0.166xw,0&resize=640:*", age=2, available=True, notes="Lorem nulla ullamco irure ut laboris. Amet do ad enim nisi irure consectetur duis aliqua.")
frances = Pet(name='Frances', species='dog', photo_url="https://www.thesprucepets.com/thmb/sfuyyLvyUx636_Oq3Fw5_mt-PIc=/3760x2820/smart/filters:no_upscale()/adorable-white-pomeranian-puppy-spitz-921029690-5c8be25d46e0fb000172effe.jpg", age=3, available=True, notes="Lorem nulla ullamco irure ut laboris. Amet do ad enim nisi irure consectetur duis aliqua.")
karley = Pet(name='Karley', species='dog', photo_url="https://i.insider.com/5484d9d1eab8ea3017b17e29?width=600&format=jpeg&auto=webp", age=4, available=True, notes="Lorem nulla ullamco irure ut laboris. Amet do ad enim nisi irure consectetur duis aliqua.")
bobby = Pet(name='Bobby', species='dog', photo_url="https://img.webmd.com/dtmcms/live/webmd/consumer_assets/site_images/article_thumbnails/other/dog_cool_summer_slideshow/1800x1200_dog_cool_summer_other.jpg", age=5, available=True, notes="Lorem nulla ullamco irure ut laboris. Amet do ad enim nisi irure consectetur duis aliqua.")
bailey = Pet(name='Bailey', species='dog', photo_url="https://www.washingtonpost.com/wp-apps/imrs.php?src=https://arc-anglerfish-washpost-prod-washpost.s3.amazonaws.com/public/HB4AT3D3IMI6TMPTWIZ74WAR54.jpg&w=1440", age=1, available=True, notes="Lorem nulla ullamco irure ut laboris. Amet do ad enim nisi irure consectetur duis aliqua.")
parker = Pet(name='Parker', species='dog', photo_url="https://scontent-lga3-2.xx.fbcdn.net/v/t1.0-9/10577011_10152711470178413_4670147788085728602_n.jpg?_nc_cat=102&ccb=2&_nc_sid=ba80b0&_nc_ohc=mRTy0PinU7EAX_fNloq&_nc_ht=scontent-lga3-2.xx&oh=f12cd96e7024d4db33d2c6b86a18401c&oe=6034673B", age=1, available=True, notes="Lorem nulla ullamco irure ut laboris. Amet do ad enim nisi irure consectetur duis aliqua.")
bell = Pet(name='Bell', species='dog', photo_url="https://scontent-lga3-2.xx.fbcdn.net/v/t1.0-9/94419093_2600295073626098_4045496590218035200_n.jpg?_nc_cat=100&ccb=2&_nc_sid=730e14&_nc_ohc=IHmulGYqHh8AX_GqPa8&_nc_ht=scontent-lga3-2.xx&oh=aa724a07d74f0a9610de2139143880ee&oe=6035797C", age=2, available=True, notes="Lorem nulla ullamco irure ut laboris. Amet do ad enim nisi irure consectetur duis aliqua.")
drake = Pet(name='Drake', species='dog', photo_url="https://scontent-lga3-2.xx.fbcdn.net/v/t1.0-9/11235338_10153840979803413_2435009813572720667_n.jpg?_nc_cat=107&ccb=2&_nc_sid=174925&_nc_ohc=TNcrFUv0VycAX8GVOvK&_nc_ht=scontent-lga3-2.xx&oh=80ce76b6101f6833de4c2cef705aed29&oe=603481C9", age=7, available=True, notes="Lorem nulla ullamco irure ut laboris. Amet do ad enim nisi irure consectetur duis aliqua.")


# Add new objects to session, so they'll persist
db.session.add(bixby)
db.session.add(frances)
db.session.add(karley)
db.session.add(bobby)
db.session.add(bailey)
db.session.add(parker)
db.session.add(bell)
db.session.add(drake)

# Commit--otherwise, this never gets saved!
db.session.commit()
