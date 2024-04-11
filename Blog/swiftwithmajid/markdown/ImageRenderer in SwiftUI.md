##  ImageRenderer in SwiftUI

18 Apr 2023

I work on a medical app where the user needs to export health data rendered
using the Swift Charts framework. It was straightforward to achieve by
leveraging the power of the new _ImageRenderer_ type. This week we will learn
how to use the _ImageRenderer_ type to export SwiftUI view as image or PDF.

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

The _ImageRenderer_ type provides an easy-to-use API, allowing us to export
the SwiftUI view hierarchy as an image. Let’s take a look at a quick example.

    
    
    import SwiftUI
    import Charts
    
    struct MyChartView: View {
        let numbers: [Double]
        
        var body: some View {
            Chart {
                ForEach(Array(numbers.enumerated()), id: \.offset) { index, value in
                    LineMark(
                        x: .value("Index", index),
                        y: .value("Value", value)
                    )
                }
            }
        }
    }
    
    struct ContentView: View {
        @StateObject private var renderer = ImageRenderer(
            content: MyChartView(
                numbers: [1,2,3]
            )
        )
        
        var body: some View {
            if let image = renderer.uiImage {
                Image(uiImage: image)
            }
        }
    }
    

As you can see in the example above, we use the _StateObject_ property wrapper
to define an instance of the _ImageRenderer_ type. The _ImageRenderer_ type
conforms to the _ObservableObject_ protocol, and SwiftUI automatically updates
the view hierarchy whenever an instance of the _ImageRenderer_ marked with the
_StateObject_ property wrapper changes.

The only parameter we need to create an instance of the _ImageRenderer_ type
is the _content_ , and it has to be a SwiftUI view. The _ImageRenderer_ type
provides us _uiImage_ and _cgImage_ properties allowing us to access the
rendered image of the content view.

In the previous example, we create an instance of the _ImageRenderer_ type by
passing an instance of the _MyChartView_ type, which uses the Swift Charts
framework to display its content. In the body of the _ContentView_ , we place
_Image_ view to show rendered version of the _MyChartView_ . As soon as the
renderer is ready, SwiftUI updates the body of the _ContentView_ .

It was a static example of using the _ImageRenderer_ type. Usually, we need to
export dynamic SwiftUI views with the data available only during app runtime.

    
    
    struct SummaryContainerView: View {
        @State private var image: UIImage?
        @State private var shareSheetShown = false
        
        var body: some View {
            List {
                summarySection
            }
            .toolbar {
                Button("Export") {
                    let renderer = ImageRenderer(content: summarySection)
                    image = renderer.uiImage
                    shareSheetShown = true
                }
            }
            .sheet(isPresented: $shareSheetShown) {
                if let image = image {
                    Image(uiImage: image)
                }
            }
        }
        
        private var summarySection: some View {
            Section {
                // ...
            }
        }
    }
    

As you can see in the example above, we render the part of the particular
SwiftUI view as an image displaying some data summary. The _ImageRenderer_
type allows us to tune a few parameters affecting the final result of the
exported image. For example, we can change the scale, size, and color mode
using the _scale_ , _proposedSize_ , and _colorMode_ properties.

    
    
    struct SummaryContainerView: View {
        @State private var image: UIImage?
        @State private var shareSheetShown = false
        @Environment(\.displayScale) private var scale
        
        var body: some View {
            List {
                summarySection
            }
            .toolbar {
                Button("Export") {
                    let renderer = ImageRenderer(content: summarySection)
                    renderer.scale = scale
                    image = renderer.uiImage
                    shareSheetShown = true
                }
            }
            .sheet(isPresented: $shareSheetShown) {
                if let image = image {
                    Image(uiImage: image)
                }
            }
        }
        
        private var summarySection: some View {
            Section {
                // ...
            }
        }
    }
    

Another exciting feature of the _ImageRenderer_ type is the ability to draw
the rendered image in any instance of the _CGContext_ type. It means you can
use the _ImageRenderer_ to make an image of SwiftUI view a part of your PDF
context.

    
    
    struct SummaryContainerView: View {
        var body: some View {
            List {
                summarySection
            }
            .toolbar {
                Button("Save as PDF") {
                    let renderer = ImageRenderer(content: summarySection)
                    renderer.render { size, renderInContext in
                        var box = CGRect(
                            origin: .zero,
                            size: .init(width: 600, height: 800)
                        )
                        
                        guard let context = CGContext(fileUrl as CFURL, mediaBox: &box, nil) else {
                            return
                        }
                        
                        context.beginPDFPage(nil)
                        renderInContext(context)
                        context.endPage()
                        context.closePDF()
                    }
                }
            }
        }
        
        private var summarySection: some View {
            Section {
                // ...
            }
        }
    }
    

As you can see in the example above, we create an instance of the _CGContext_
to generate a PDF file. We use the _render_ function of the _ImageRenderer_
type allowing us to access the size of the image displaying a SwiftUI view,
and the renderer function that we can use to inject the image into an instance
of the _CGContext_ type.

I hope you enjoy the post. Feel free to follow me on [ Twitter
](https://twitter.com/mecid) and ask your questions related to this post.
Thanks for reading, and see you next week!

