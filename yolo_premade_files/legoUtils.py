import cv2;
import pandas as pd;
import threading;
import time;
import datetime

# from utils.rpiutils import BinaryLEDController

class TwoBitBranchPredictor:
        def __init__(self, PATH_TO_CSV):
                self.columns = ['id', 'name', 'part', 'count', 'section']
                self.csv = pd.read_csv(PATH_TO_CSV, header=0,usecols=self.columns)
                self.names = self.csv['name']
                self.ids = self.csv['id']
                self.parts = self.csv['part']
                self.counts = self.csv['count']
                self.sections = self.csv['section']
                self.led_pins = [4, 17, 18, 27]
                self.sectionMap = {}
                self.currentSection = 15
                # self.rpiConnection = BinaryLEDController(self.led_pins)
                self.nameMap ={}
                self.periodic_check()
                for i, section in enumerate(self.sections):
                        if section not in self.sectionMap:
                                self.sectionMap[section] = {'count': 0, 'section': section}
                self.sectionMap[15] = {'count': 0, 'section': 15}
                
                for i, name in enumerate(self.names):
                        if name not in self.nameMap:
                                self.nameMap[name] = {'name': name, 'section': self.sections[i]}
                self.nameMap['None'] = {'count': 0, 'section': 15}
        
        def periodic_check(self):
                
                def check_currentSection():
                        while True:
                                print(f"Current time: {datetime.datetime.now()}, Current section: {self.currentSection}")
                                # self.rpiConnection.set_current_value(self.currentSection)
                                time.sleep(1)
                
                check_thread = threading.Thread(target=check_currentSection, daemon=True)
                check_thread.start()

        def __str__(self):
                return f"TwoBitBranchPredictor( sections: {self.sectionMap} \n names: {self.nameMap})"
    
        def predict(self, objectName):
                predictedSection = self.nameMap.get(objectName).get('section')
                for section, data in self.sectionMap.items():
                        if predictedSection == section:
                                if data['count'] < 3:
                                        data['count'] += 1
                        else:
                                if data['count'] > 0:
                                        data['count'] -= 1
                
                for section, data in self.sectionMap. items():
                        if data['count'] >= 3:
                                self.currentSection = section
    


def draw_vertical_zones(image, zone_width, zone_height, color=(0, 255, 0), thickness=2):
        img_height, img_width, _ = image.shape
        
        # Calculate the starting x-coordinates for the three zones
        zone1_x = int(img_width * 1/6 - zone_width / 2)
        zone2_x = int(img_width * 3/6 - zone_width / 2)
        zone3_x = int(img_width * 5/6 - zone_width / 2)

        # Calculate the starting y-coordinate for the zones
        zone_y = int(img_height / 2 - zone_height / 2)

        # Draw the three vertical rectangles
        cv2.rectangle(image, (zone1_x, zone_y), (zone1_x + zone_width, zone_y + zone_height), color, thickness)
        cv2.rectangle(image, (zone2_x, zone_y), (zone2_x + zone_width, zone_y + zone_height), color, thickness)
        cv2.rectangle(image, (zone3_x, zone_y), (zone3_x + zone_width, zone_y + zone_height), color, thickness)

        return image