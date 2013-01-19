//
//  LocationAwareness.h
//
//  Created by Joel Smith on 4/3/12.
//  Copyright (c) 2012 Trosic. All rights reserved.
//
// This is a simple wrapper class for the GPS in iOS that provides location data and reverse geolocation.
// It also has a simple property that updates when GPS location has been established.

#import <Foundation/Foundation.h>
#import <CoreLocation/CoreLocation.h>
#import <MapKit/MapKit.h>

@interface LocationAwareness : NSObject <CLLocationManagerDelegate> {
    CLLocationManager *locationManager;
}
@property(nonatomic, strong) NSString *longitude;
@property(nonatomic, strong) NSString *latitude;
@property(nonatomic, strong) NSString *city;
@property(nonatomic, strong) NSString *state;
@property(nonatomic, strong) NSString *zip;
@property(nonatomic, strong) NSString *country;
@property (nonatomic, strong) CLPlacemark *placemark;
@property (nonatomic, assign) BOOL isupdated;



@end
