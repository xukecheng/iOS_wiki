##  Mastering MapKit in SwiftUI. Basics.

28 Nov 2023

MapKit integration with SwiftUI significantly changed this year. In the
previous version of SwiftUI, we had very basic functionality of _MKMapView_
wrapped into the SwiftUI view named _Map_ . Fortunately, things changed, and
SwiftUI introduced a new API for MapKit integration. This week, we will learn
how to use the new full-featured APIs available in the latest iteration of
SwiftUI to integrate with MapKit.

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

As I said before, in the previous versions of the SwiftUI framework, we had a
_Map_ view providing us with basic functionality for MapKit, which is
deprecated now. Using the deprecated Map view still makes sense whenever you
target previous versions of Apple platforms.

> To learn more about the old MapKit integration with SwiftUI, take a look at
> my dedicated [ “Using MapKit with SwiftUI” ](/2020/07/29/using-mapkit-with-
> swiftui/) post.

The new MapKit API introduces the _MapContentBuilder_ result builder that
looks similar to the _ViewBuilder_ but instead uses the types conforming to
the _MapContent_ protocol. Let’s start with the basic example of using the new
MapKit APIs in SwiftUI.

    
    
    import MapKit
    import SwiftUI
    
    extension CLLocationCoordinate2D {
        static let newYork: Self = .init(
            latitude: 40.730610,
            longitude: -73.935242
        )
        
        static let seattle: Self = .init(
            latitude: 47.608013,
            longitude: -122.335167
        )
        
        static let sanFrancisco: Self = .init(
            latitude: 37.733795,
            longitude: -122.446747
        )
    }
    
    struct ContentView: View {
        var body: some View {
            Map {
                Annotation("Seattle", coordinate: .seattle) {
                    Image(systemName: "mappin")
                        .foregroundStyle(.black)
                        .padding()
                        .background(.red)
                        .clipShape(Circle())
                }
                
                Marker(coordinate: .newYork) {
                    Label("New York", systemImage: "mappin")
                }
                
                Marker("San Francisco", monogram: Text("SF"), coordinate: .sanFrancisco)
            }
        }
    }
    

As you can see in the example above, we define the map and place the content
on it by using the _MapContentBuilder_ closure. The _MapContentBuilder_ type
works with any type conforming to the _MapContent_ protocol.

![map-with-markers](/public/map3.png)

In our example, we use _Marker_ and _Annotation_ types. The _Marker_ is the
essential item that allows us to place a predefined pin on the map. The
_Annotation_ type is more advanced and will enable us to place a SwiftUI view
on the map using the latitude and longitude.

SwiftUI provides us with a bunch of types conforming to the _MapContent_
protocol. We already used two of them: _Marker_ and _Annotation_ . Many of
them include _MapCircle_ , _MapPolygon_ , _MapPolyline_ , _UserAnnotation_ ,
etc.

    
    
    struct ContentView: View {
        var body: some View {
            Map {
                Annotation("Seattle", coordinate: .seattle) {
                    Image(systemName: "mappin")
                        .foregroundStyle(.black)
                        .padding()
                        .background(.red)
                        .clipShape(Circle())
                }
                
                Marker(coordinate: .newYork) {
                    Label("New York", systemImage: "mappin")
                }
                
                UserAnnotation()
            }
        }
    }
    

You can control the initial position of the map by using another overload of
the Map initializer that provides the _initialPosition_ parameter.

    
    
    struct ContentView: View {
        let initialPosition: MapCameraPosition = .userLocation(
            fallback: .camera(
                MapCamera(centerCoordinate: .newYork, distance: 0)
            )
        )
        
        var body: some View {
            Map(initialPosition: initialPosition) {
                Annotation("Seattle", coordinate: .seattle) {
                    Image(systemName: "mappin")
                        .foregroundStyle(.black)
                        .padding()
                        .background(.red)
                        .clipShape(Circle())
                }
                
                Marker(coordinate: .newYork) {
                    Label("New York", systemImage: "mappin")
                }
                
                Marker("San Francisco", monogram: Text("SF"), coordinate: .sanFrancisco)
            }
        }
    }
    

The _initialPosition_ parameter takes an instance of the _MapCameraPosition_
type. The _MapCameraPosition_ allows us to define the map position in a few
ways. It can be the user location that we use in our example, or you can point
it to any area on the map using the _camera_ , _region_ , _rect_ , or _item_
static functions. By default, it uses the _automatic_ instance of the
_MapCameraPosition_ type that fits the map content.

Whenever you need constant control over the camera position, you can use
another overload of the _Map_ initializer, allowing you to provide two-way
binding to the map camera position.

    
    
    struct ContentView: View {
        @State private var position: MapCameraPosition = .userLocation(
            fallback: .camera(
                MapCamera(centerCoordinate: .newYork, distance: 0)
            )
        )
        
        var body: some View {
            Map(position: $position) {
                // ...
            }
        }
    }
    

SwiftUI updates the position binding once the user drags the map. It also
updates the map camera position as soon as you update the position property
programmatically.

    
    
    struct ContentView: View {
        @State private var position: MapCameraPosition = .userLocation(
            fallback: .camera(
                MapCamera(centerCoordinate: .newYork, distance: 0)
            )
        )
        
        var body: some View {
            Map(position: $position, interactionModes: .pitch) {
                // ...
            }
        }
    }
    

You can control the types of interactions allowed with the map by using the
_interactionModes_ parameters. The _MapInteractionModes_ type defines a set of
interactions like _pan_ , _pitch_ , _rotate_ and _zoom_ . By default, it
enables all the available interaction types.

Today, we learned the basics of the MapKit integration in SwiftUI. We will
continue the topic in the upcoming weeks by covering camera manipulations, map
controls, and other advanced topics. I hope you enjoy the post. Feel free to
follow me on [ Twitter ](https://twitter.com/mecid) and ask your questions
related to this post. Thanks for reading, and see you next week!

  1. Mastering MapKit in SwiftUI. Basics. 
  2. [ Mastering MapKit in SwiftUI. Customizations. ](/2023/12/05/mastering-mapkit-in-swiftui-customizations/)
  3. [ Mastering MapKit in SwiftUI. Camera. ](/2023/12/12/mastering-mapkit-in-swiftui-camera/)
  4. [ Mastering MapKit in SwiftUI. Interactions. ](/2023/12/19/mastering-mapkit-in-swiftui-interactions/)

