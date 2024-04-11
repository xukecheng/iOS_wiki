##  Using UIKit views in SwiftUI

29 Jan 2020

A few weeks ago, we talked about building views like [ _PagerView_
](/2019/12/25/building-pager-view-in-swiftui/) and [ _BottomSheetView_
](/2019/12/11/building-bottom-sheet-in-swiftui/) from scratch in SwiftUI.
SwiftUI is pretty young and misses some components that we expect to have out
of the box. But it provides all the needed APIs to build whatever we want.
However, sometimes we need to reuse _UIKit_ views instead of making the
SwiftUI versions. This week I want to talk to you about using _UIKit_ views in
SwiftUI.

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

####  UIViewRepresentable

One of the good examples of _UIKit_ views that we don’t want to recreate in
SwiftUI is _MKMapView_ . Do you have any ideas on how to implement it in
SwiftUI from scratch? Happily, we don’t need to do that. We can easily use
_MKMapView_ in SwiftUI by simply creating a wrapper view.

SwiftUI provides us _UIViewRepresentable_ protocol that allows us to wrap
_UIKit_ views and use them from SwiftUI views. Let’s take a look at how we can
cover _MKMapView_ to use it in SwiftUI.

    
    
    struct MapView: UIViewRepresentable {
        typealias UIViewType = MKMapView
    
        func makeUIView(context: UIViewRepresentableContext<MapView>) -> MKMapView {
            MKMapView()
        }
    
        func updateUIView(_ uiView: MKMapView, context: UIViewRepresentableContext<MapView>) {
        }
    }
    

As you can see in the example above, we create a _MapView_ struct that
conforms to the _UIViewRepresentable_ protocol. _UIViewRepresentable_ protocol
has two requirements: _makeUIView_ and _updateUIView_ methods.

SwiftUI calls _makeUIView_ only one time when it creates a view hierarchy.
Whenever you change the state of the view, SwiftUI calls _updateUIView_ method
to update the view according to state changes.

Let’s ignore state changes for now and just create an empty _MKMapView_ .
Finally, we can use our _MapView_ in SwiftUI.

    
    
    struct RootView: View {
        var body: some View {
            MapView()
                .edgesIgnoringSafeArea(.all)
        }
    }
    

####  State and Binding

_UIViewRepresentable_ view can store a state or has a binding like any other
SwiftUI components. Let’s refactor our _MapView_ to accept a binding for a
center coordinate via init method.

    
    
    struct MapView: UIViewRepresentable {
        typealias UIViewType = MKMapView
    
        @Binding var center: CLLocationCoordinate2D
    
        func makeUIView(context: UIViewRepresentableContext<MapView>) -> MKMapView {
            MKMapView()
        }
    
        func updateUIView(_ uiView: MKMapView, context: UIViewRepresentableContext<MapView>) {
            uiView.setCenter(center, animated: true)
        }
    }
    

As you can see in the example above, we finally implemented _updateUIView_ .
We want to center our map view whenever the binding of the center location
changed.

####  Coordinator

_UIKit_ views usually have delegates that allow us to handle some user
interactions like cell selection in _UITableView_ or visible region changes in
_MKMapView_ . What if we want to handle these actions in SwiftUI? Fortunately,
_UIViewRepresentable_ provides a **Coordinator** object that allows us to deal
with delegates, data sources, and other _UIKit_ stuff. The coordinator is a
bridge between your _UIKit_ and SwiftUI views. Let’s see how we can use it.

    
    
    struct MapView: UIViewRepresentable {
        typealias UIViewType = MKMapView
    
        @Binding var center: CLLocationCoordinate2D
    
        func makeUIView(context: UIViewRepresentableContext<MapView>) -> MKMapView {
            let mapView = MKMapView()
            mapView.delegate = context.coordinator
            return mapView
        }
    
        func updateUIView(_ uiView: MKMapView, context: UIViewRepresentableContext<MapView>) {
            uiView.setCenter(center, animated: true)
        }
    
        func makeCoordinator() -> MapView.Coordinator {
            Coordinator(self)
        }
    
        final class Coordinator: NSObject, MKMapViewDelegate {
            private let mapView: MapView
    
            init(_ mapView: MapView) {
                self.mapView = mapView
            }
    
            func mapView(_ mapView: MKMapView, regionDidChangeAnimated animated: Bool) {
                self.mapView.center = mapView.centerCoordinate
            }
        }
    }
    

_UIViewRepresentable_ has an optional requirement to implement
_makeCoordinator_ method. This method should create and return a coordinator
object. We can fulfill all the needed delegate methods using this object. As
you can see in the example above, we want to update our binding whenever the
user moves the map. We might need to add some pins based on location changes.

####  Conclusion

This week we learned how to use _UIKit_ views in SwiftUI. SwiftUI is a great
framework, but sometimes we need to reuse _UIKit_ classes that we had for
years in _iOS SDK_ . Fortunately, it is very effortless to do with help of
_UIViewRepresentable_ protocol. I hope you enjoy the post. Feel free to follow
me on [ Twitter ](https://twitter.com/mecid) and ask your questions related to
this post. Thanks for reading, and see you next week!

