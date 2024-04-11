##  Mastering MapKit in SwiftUI. Camera.

12 Dec 2023

In this post, we will continue the topic of the new MapKit API in SwiftUI. We
will cover one of the most critical cases of displaying a map. This week, we
will learn about camera position and map bounds.

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

####  Map bounds

The new MapKit API introduces the _MapCameraBounds_ type, allowing us to limit
the bounds of the map view. The _MapCameraBounds_ type has a few initializers
that we can use to create camera bounds from the instance of _MKMapRect_ or
_MKCoordinateRegion_ .

    
    
    extension CLLocationCoordinate2D {
        static let newYork: Self = .init(
            latitude: 40.730610,
            longitude: -73.935242
        )
    }
    
    let rect = MKMapRect(
        origin: MKMapPoint(.newYork),
        size: MKMapSize(width: 1, height: 1)
    )
    
    struct ContentView: View {
        var body: some View {
            Map(bounds: MapCameraBounds(centerCoordinateBounds: rect)) {
                Marker("New York", monogram: Text("NY"), coordinate: .newYork)
            }
        }
    }
    

As you can see in the example above, we use the _MKMapRect_ type to define the
visible bounds of the map that user can’t leave by using any interaction.

To create an instance of the _MKMapRect_ type, we should call the initializer
with _origin_ and _size_ parameters. We can use any instance of the
_CLLocationCoordinate2D_ type to define an origin point. The second parameter
must be an instance of the _MKMapSize_ , representing the width and height in
map points.

Now, we can use an instance of the _MKMapRect_ type to pass into the
initializer of the _MapCameraBounds_ type to limit our map to a particular
rectangle. We can also allow users to zoom in or out to a limited amount of
meters using _maximumDistance_ and _minimumDistance_ parameters of the
_MapCameraBounds_ initializer.

    
    
    struct ContentView: View {
        var body: some View {
            Map(
                bounds: MapCameraBounds(
                    centerCoordinateBounds: rect,
                    minimumDistance: 10,
                    maximumDistance: 100
                )
            ) {
                Marker("New York", monogram: Text("NY"), coordinate: .newYork)
            }
        }
    }
    

You may have a set of coordinates you want to zoom in and limit to the
rectangle displaying these markers. In this case, you can create an instance
of the _MKMapRect_ type per coordinate and use the _union_ function on the
_MKMapRect_ type to create a rectangle including all the coordinates.

    
    
    let coordinates: [CLLocationCoordinate2D] = [.newYork, .sanFrancisco, .seattle]
    let rect = coordinates
        .map { MKMapRect(origin: .init($0), size: .init(width: 1, height: 1)) }
        .reduce(MKMapRect.null) { $0.union($1) }
    

We discussed how to use the _MKMapRect_ in pair with the _MapCameraBounds_
type to limit our map to a particular rectangle. The _MKMapRect_ uses map
points to represent a rectangle. _MKMapPoint_ uses the 2D projection of the
map on a flat surface to calculate x and y on the map. You can use _x_ , _y_ ,
and _coordinate_ properties of the _MKMapPoint_ type to convert coordinates to
map points and back.

Whenever you want to use latitude and longitude deltas instead of map points,
you can use the _MKCoordinateRegion_ type. It provides functionality similar
to _MKMapRect_ but operates on other units.

####  Map camera position

The MapKit provides the _MapCameraPosition_ type that we can use for two-way
binding of the recently visible camera position. We can create an instance of
the _MapCameraPosition_ type by passing _MKMapRect_ , _MKCoordinateRegion_ ,
_MKMapItem_ , _CLLocationCoordinate2D_ , etc.

    
    
    struct ContentView: View {
        @State private var position: MapCameraPosition = .camera(
            .init(centerCoordinate: .newYork, distance: 0)
        )
        
        var body: some View {
            Map(
                position: $position,
                bounds: MapCameraBounds(
                    centerCoordinateBounds: rect,
                    minimumDistance: 10,
                    maximumDistance: 100
                )
            ) {
                Marker("New York", monogram: Text("NY"), coordinate: .newYork)
            }
            .onAppear {
                position = .camera(.init(centerCoordinate: .sf, distance: 0))
            }
        }
    }
    

We can also use the _MapCameraPosition_ type to ask for a map view to follow
the user location.

    
    
    struct ContentView: View {
        @State private var position: MapCameraPosition = .userLocation(
            followsHeading: true,
            fallback: .rect(rect)
        )
        
        var body: some View {
            Map(
                position: $position,
                bounds: MapCameraBounds(
                    centerCoordinateBounds: rect,
                    minimumDistance: 10,
                    maximumDistance: 100
                )
            ) {
                Marker("New York", monogram: Text("NY"), coordinate: .newYork)
            }
        }
    }
    

As I said before, we can use _MapCameraPosition_ for two-way binding, which
means we can query an instance of the _MapCameraPosition_ type to read some
data.

    
    
    struct ContentView: View {
        @State private var position: MapCameraPosition = .rect(
            MKMapRect(
                origin: MKMapPoint(.newYork),
                size: MKMapSize(width: 1, height: 1)
            )
        )
        
        var body: some View {
            Map(
                position: $position,
                bounds: MapCameraBounds(
                    centerCoordinateBounds: rect,
                    minimumDistance: 10,
                    maximumDistance: 100
                )
            ) {
                Marker("New York", monogram: Text("NY"), coordinate: .newYork)
            }
            .onChange(of: position) {
                print(position.positionedByUser)
                print(position.camera)
                print(position.region)
                print(position.rect)
            }
            .onAppear {
                position = .camera(.init(centerCoordinate: .newYork, distance: 0))
            }
        }
    }
    

As you can see in the example above, we use an instance of the
_MapCameraPosition_ to access the recent camera, region, rectangle, etc, of
the map. All of the mentioned fields are optional and will be non-nil values
if the particular instance of the _MapCameraPosition_ type is used.

There is also the _positionedByUser_ property. It is a boolean value defining
whenever the camera is positioned by the user or positioned by the developer
programmatically.

Today, we learned how to manage the map camera position using the new
_MapCameraPosition_ type, part of the new rich MapKit API. I hope you enjoy
the post. Feel free to follow me on [ Twitter ](https://twitter.com/mecid) and
ask your questions related to this post. Thanks for reading, and see you next
week!

  1. [ Mastering MapKit in SwiftUI. Basics. ](/2023/11/28/mastering-mapkit-in-swiftui-basics/)
  2. [ Mastering MapKit in SwiftUI. Customizations. ](/2023/12/05/mastering-mapkit-in-swiftui-customizations/)
  3. Mastering MapKit in SwiftUI. Camera. 
  4. [ Mastering MapKit in SwiftUI. Interactions. ](/2023/12/19/mastering-mapkit-in-swiftui-interactions/)

