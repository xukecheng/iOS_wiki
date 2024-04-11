##  Mastering MapKit in SwiftUI. Customizations.

05 Dec 2023

Last week, we started a series of posts about the new MapKit API in SwiftUI.
We talked about the basics of the new API, and now we can continue the topic
by covering the customization part of new APIs. This week, we will learn the
customization points of MapKit API in SwiftUI.

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

####  Map style

The new MapKit API introduces the _mapStyle_ view modifier, allowing us to
customize the style of the data presented on the map.

    
    
    struct ContentView: View {
        var body: some View {
            Map {
                // ...
            }
            .mapStyle(.imagery(elevation: .realistic))
        }
    }
    

As you can see in the example above, we use the _mapStyle_ view modifier with
the _imagery_ style and realistic elevation. Another option for the elevation
parameter of the imagery style is flat.

![imagery-map](/public/map4.png)

SwiftUI provides us with a set of predefined and configurable map styles. In
the previous example, we used a style called _imagery_ . By default, the
SwiftUI framework uses the _standard_ style. The standard style allows us to
configure the elevation of the map, points of interest we want to include or
exclude from the map, and whenever we need to show traffic.

    
    
    struct ContentView: View {
        var body: some View {
            Map {
                // ...
            }
            .mapStyle(
                .standard(
                    elevation: .flat,
                    pointsOfInterest: .excluding([.store]),
                    showsTraffic: false
                )
            )
        }
    }
    

Another option is the _hybrid_ style, allowing us to display imagery, roads,
and road names on the map. The hybrid style also configures elevation,
traffic, and points of interest.

    
    
    struct ContentView: View {
        var body: some View {
            Map {
                // ...
            }
            .mapStyle(
                .hybrid(
                    elevation: .flat,
                    pointsOfInterest: .including([.airport]),
                    showsTraffic: true
                )
            )
        }
    }
    

####  Map interactions

MapKit supports different types of interactions with the map. You can _zoom_ ,
_pan_ , _pitch_ , and _rotate_ the content on the map. By default, SwiftUI
activates all of the available gestures. But you can easily limit available
interactions to the list of the preferred ones.

    
    
    struct ContentView: View {
        var body: some View {
            Map(interactionModes: [.pan, .pitch]) {
                // ...
            }
        }
    }
    

####  Map controls

Whenever you import MapKit in pair with SwiftUI, you will get access to the
particular SwiftUI views you can use as map controls. These views include
_MapScaleView_ , _MapCompass_ , _MapPitchToggle_ , _MapUserLocationButton_ ,
and _MapZoomStepper_ views.

    
    
    struct ContentView: View {
        var body: some View {
            Map {
                // ...
            }
            .mapControls {
                MapScaleView()
                MapCompass()
            }
        }
    }
    

You can use these views in pair with the _mapControls_ view modifier to
specify controls for any map instances sharing the same environment in the
SwiftUI view hierarchy.

Whenever you place _MapScaleView_ or _MapCompass_ views inside the
_mapControls_ view modifier, you allow SwiftUI to control the placement of the
map controls. In this case, SwiftUI decides the placement of the control
depending on the platform running the app.

As you may have noticed, _MapScaleView_ and other map controls are simple
SwiftUI views, which means you can use them outside of the _mapControls_ view
modifier anywhere you want. In this case, to bind a map control to a
particular map instance, you should use the _mapScope_ view modifier.

    
    
    struct MapScopeExample: View {
        @Namespace private var favoritesMap
        var body: some View {
            VStack {
                Map(scope: favoritesMap) {
                    // favorite pins
                }
                
                HStack {
                    MapScaleView(scope: favoritesMap)
                    MapCompass(scope: favoritesMap)
                }
            }
            .mapScope(favoritesMap)
        }
    }
    

As you can see in the example above, we use _Namespace_ property wrapper to
generate a map identifier to bind controls to the map instance. You can also
use the _mapControlVisibility_ view modifier when you need to change the
automatic visibility configuration to always visible or hidden.

    
    
    struct MapScopeExample: View {
        @Namespace private var favoritesMap
        var body: some View {
            VStack {
                Map(scope: favoritesMap) {
                    // favorite pins
                }
                
                HStack {
                    MapScaleView(scope: favoritesMap)
                    MapCompass(scope: favoritesMap)
                        .mapControlVisibility(.hidden)
                }
            }
            .mapScope(favoritesMap)
        }
    }
    

Today, we learned how to customize map presentation in SwiftUI. SwiftUI
provides a flexible and easy-to-use API for configuring map controls, styles,
and interaction modes. I hope you enjoy the post. Feel free to follow me on [
Twitter ](https://twitter.com/mecid) and ask your questions related to this
post. Thanks for reading, and see you next week!

  1. [ Mastering MapKit in SwiftUI. Basics. ](/2023/11/28/mastering-mapkit-in-swiftui-basics/)
  2. Mastering MapKit in SwiftUI. Customizations. 
  3. [ Mastering MapKit in SwiftUI. Camera. ](/2023/12/12/mastering-mapkit-in-swiftui-camera/)
  4. [ Mastering MapKit in SwiftUI. Interactions. ](/2023/12/19/mastering-mapkit-in-swiftui-interactions/)

