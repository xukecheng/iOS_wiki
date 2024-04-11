##  Mastering MapKit in SwiftUI. Interactions.

19 Dec 2023

MapKit provides us with a very rich API as part of the next iteration of the
SwiftUI framework. This week, we will continue the topic by learning how to
handle interactions using the new MapKit API in SwiftUI.

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

In the previous post, we discussed the map view’s camera position. Let me
update your memory with the quick code example.

    
    
    struct ContentView: View {
        @State private var position: MapCameraPosition = .camera(
            .init(centerCoordinate: .newYork, distance: 10_000_000)
        )
        
        var body: some View {
            Map(position: $position) {
                Marker("New York", monogram: Text("NY"), coordinate: .newYork)
                Marker("Seattle", monogram: Text("SE"), coordinate: .seattle)
                Marker("San Francisco", monogram: Text("SF"), coordinate: .sanFrancisco)
            }
            .onChange(of: position) {
                print(position.camera?.centerCoordinate)
                print(position.positionedByUser)
            }
        }
    }
    

As you can see in the example above, we use the _onChange_ view modifier to
track changes in the two-way binding of the camera position. Unfortunately, we
can’t get the direct camera position from the binding in the case of user
drag. For this particular case, MapKit API introduces the _onMapCameraChange_
view modifier.

    
    
    struct ContentView: View {
        @State private var position: MapCameraPosition = .camera(
            .init(centerCoordinate: .newYork, distance: 10_000_000)
        )
        
        var body: some View {
            Map(position: $position) {
                Marker("New York", monogram: Text("NY"), coordinate: .newYork)
                Marker("Seattle", monogram: Text("SE"), coordinate: .seattle)
                Marker("San Francisco", monogram: Text("SF"), coordinate: .sanFrancisco)
            }
            .onMapCameraChange(frequency: .continuous) { context in
                print(context.camera)
                print(context.region)
                print(context.rect)
            }
        }
    }
    

In the example above, we use the _onMapCameraChange_ view modifier to track
camera changes as soon as the camera position changes. MapKit API allows us to
set the frequency of the _onMapCameraChange_ listener by passing an instance
of the _MapCameraUpdateFrequency_ type.

The _MapCameraUpdateFrequency_ enum provides us with two options: _continuous_
and _onEnd_ . The first defines nearly real-time changes in the camera
position. The second fires whenever the camera position drags finish.

    
    
    struct ContentView: View {
        @State private var position: MapCameraPosition = .camera(
            .init(centerCoordinate: .newYork, distance: 10_000_000)
        )
        
        var body: some View {
            Map(position: $position) {
                Marker("New York", monogram: Text("NY"), coordinate: .newYork)
                Marker("Seattle", monogram: Text("SE"), coordinate: .seattle)
                Marker("San Francisco", monogram: Text("SF"), coordinate: .sanFrancisco)
            }
            .onMapCameraChange(frequency: .onEnd) { context in
                print(context.camera)
                print(context.region)
                print(context.rect)
            }
        }
    }
    

The second parameter of the _onMapCameraChange_ view modifier is the action
closure, which can handle camera position updates. The action closure provides
us with an instance of the _MapCameraUpdateContext_ type defining the current
map camera, rectangle, and region.

The new MapKit API also introduces the _mapCameraKeyframeAnimator_ view
modifier, allowing us to animate the map camera using a keyframe animator.

    
    
    struct ContentView: View {
        @State private var trigger = false
        @State private var position: MapCameraPosition = .camera(
            .init(centerCoordinate: .newYork, distance: 10_000_000)
        )
        
        var body: some View {
            Map(position: $position) {
                Marker("New York", monogram: Text("NY"), coordinate: .newYork)
                Marker("Seattle", monogram: Text("SE"), coordinate: .seattle)
                Marker("San Francisco", monogram: Text("SF"), coordinate: .sanFrancisco)
            }
            .mapCameraKeyframeAnimator(trigger: trigger) { camera in
                KeyframeTrack(\MapCamera.centerCoordinate) {
                    LinearKeyframe(.newYork, duration: 2)
                    LinearKeyframe(.seattle, duration: 2)
                    LinearKeyframe(.sanFrancisco, duration: 2)
                }
                
                KeyframeTrack(\MapCamera.distance) {
                    LinearKeyframe(camera.distance, duration: 2)
                    LinearKeyframe(camera.distance * 2, duration: 2)
                    LinearKeyframe(camera.distance, duration: 2)
                }
            }
            .task {
                trigger.toggle()
            }
        }
    }
    

As you can see in the example above, we use the _mapCameraKeyframeAnimator_
view modifier to define a trigger value. Trigger value allows us to animate
the map camera whenever the trigger value changes.

The second parameter of the _mapCameraKeyframeAnimator_ view modifier is the
_KeyframesBuilder_ closure, which allows us to define a set of keyframe
tracks. Inside these tracks, we describe the transition states to iterate our
animation.

As you can see, we can animate all the properties of the _MapCamera_ type. In
our example, we animate the map camera’s center location and distance. The
_KeyframesBuilder_ closure also provides us with the initial value of the map
camera, allowing us to read the value of the map camera before animation.

Last, the topic to cover is the map selection feature. The _Map_ view provides
an initializer with a _selection_ parameter, allowing us to offer a two-way
binding for map content selection.

    
    
    struct ContentView: View {
        @State private var selection: Int?
        @State private var position: MapCameraPosition = .camera(
            .init(centerCoordinate: .newYork, distance: 10_000_000)
        )
        
        var body: some View {
            Map(position: $position, selection: $selection) {
                Marker("New York", monogram: Text("NY"), coordinate: .newYork)
                    .tag(1)
                Marker("Seattle", monogram: Text("SE"), coordinate: .seattle)
                    .tag(2)
                Marker("San Francisco", monogram: Text("SF"), coordinate: .sanFrancisco)
                    .tag(3)
            }
            .onChange(of: selection) {
                print("selection changed:", selection)
            }
        }
    }
    

In the example above, we define a state property to store the currently
selected value of the map. We also annotate our markers using the _tag_ view
modifier. Remember that the type of the _selection_ property must be the same
as the _tag_ you provide to the map content.

Today, we learned how to handle interactions on the map using the set of new
view modifiers which is the part of the new rich MapKit API in SwiftUI. I hope
you enjoy the post. Feel free to follow me on [ Twitter
](https://twitter.com/mecid) and ask your questions related to this post.
Thanks for reading, and see you next week!

  1. [ Mastering MapKit in SwiftUI. Basics. ](/2023/11/28/mastering-mapkit-in-swiftui-basics/)
  2. [ Mastering MapKit in SwiftUI. Customizations. ](/2023/12/05/mastering-mapkit-in-swiftui-customizations/)
  3. [ Mastering MapKit in SwiftUI. Camera. ](/2023/12/12/mastering-mapkit-in-swiftui-camera/)
  4. Mastering MapKit in SwiftUI. Interactions. 

