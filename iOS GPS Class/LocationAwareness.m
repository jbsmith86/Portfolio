//
//  LocationAwareness.m
//
//  Created by Joel Smith on 4/3/12.
//  Copyright (c) 2012 Trosic. All rights reserved.
//

#import "LocationAwareness.h"

@implementation LocationAwareness
@synthesize longitude;
@synthesize latitude;
@synthesize city;
@synthesize state;
@synthesize zip;
@synthesize country;
@synthesize placemark;
@synthesize isupdated;

- (id)init {
    locationManager = [[CLLocationManager alloc] init];
    locationManager.delegate = self;
    locationManager.desiredAccuracy = kCLLocationAccuracyHundredMeters;
    [locationManager startUpdatingLocation];
    return self;
}
    
- (void)locationManager:(CLLocationManager *)manager didUpdateToLocation:(CLLocation *)newLocation fromLocation:(CLLocation *)oldLocation {
            
            [locationManager stopUpdatingLocation];
            self.latitude = [NSString stringWithFormat:@"%f", newLocation.coordinate.latitude];
            self.longitude = [NSString stringWithFormat:@"%f", newLocation.coordinate.longitude];
            [self gpsIsUpdated];
}


- (void)gpsIsUpdated {
    [self reverseLocation];
}

- (void)reverseLocation {
    CLGeocoder *clgeo = [[CLGeocoder alloc]init];
    [clgeo reverseGeocodeLocation:locationManager.location completionHandler:
     ^(NSArray *placemarks, NSError *error) {
         self.placemark = [placemarks objectAtIndex:0];
         self.city = self.placemark.locality;
         self.state = self.placemark.administrativeArea;
         self.zip = self.placemark.postalCode;
         self.country = self.placemark.country;
         self.isupdated = YES;
     }];
}

@end
