//
//  LocationAwareness.h
//
//  Created by Joel Smith on 4/3/12.
//  Copyright (c) 2012 Trosic. All rights reserved.
//

#import <Foundation/Foundation.h>
#import <CoreLocation/CoreLocation.h>
#import <MapKit/MapKit.h>
#import "RXMLElement.h"

@interface LocationAwareness : NSObject <CLLocationManagerDelegate> {
    CLLocationManager *locationManager;
    //MKReverseGeocoder *geocoder;
}
@property(nonatomic, strong) NSString *longitude;
@property(nonatomic, strong) NSString *latitude;
@property(nonatomic, strong) NSString *city;
@property(nonatomic, strong) NSString *state;
@property(nonatomic, strong) NSString *zip;
@property(nonatomic, strong) NSString *country;
@property (nonatomic, strong) CLPlacemark *placemark;
@property (nonatomic, assign) BOOL isupdated;

//@property (nonatomic) CLLocationCoordinate2D coord;

@end
