##  Mastering charts in SwiftUI. Customizations.

15 Feb 2023

The Swift Charts framework became a huge topic on my blog. But I decided to
continue this subject to cover everything I’ve experienced with the Charts
framework. This week we will learn how to customize the _Chart_ view using a
bunch of chart view modifiers provided by the framework.

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

####  Plot area

The first thing you might need is the tuning plot area of the _Chart_ view.
The Charts framework provides the _chartPlotStyle_ view modifier allowing us
to style the view representing the chart’s plot area. Let’s take a look at how
we can use it.

    
    
    struct ContentView: View {
        var body: some View {
            Chart {
                // ...
            }
            .chartPlotStyle { chartContent in
                chartContent
                    .background(Color.secondary.opacity(0.2))
                    .frame(height: 32)
                
            }
        }
    }
    

As you can see in the example above, we use the _chartPlotStyle_ view modifier
to access the chart’s content view. It is a simple SwiftUI view, meaning we
can apply any view modifiers we need. In our case, we use the _frame_ view
modifier to set a particular height and the _background_ view modifier to fill
the background with a gray color.

![stacked-bar-chart](/public/chart14.png)

As you know, the _Chart_ view is also a SwiftUI view, and we can apply the
_frame_ view modifier to it, but in this case, it will affect the whole chart
view with its legend view, which is not a good idea.

> To learn more about the basics of the Charts framework, take a look at my
> dedicated [ “Mastering charts in SwiftUI. Basics.” ](/2023/01/10/mastering-
> charts-in-swiftui-basics/) post.

####  Axis

The Charts framework provides us _chartXAxis_ and _chartYAxis_ view modifiers
allowing us to control the look and feel of the particular axis completely.
These view modifiers accept _AxisContentBuilder_ closure, where we can define
how we want to build the axis.

    
    
    struct ContentView: View {
        var body: some View {
            Chart {
                // ...
            }
            .chartXAxis {
                AxisMarks(
                    preset: .aligned,
                    position: .bottom,
                    values: .stride(by: 500),
                    stroke: StrokeStyle(
                        lineWidth: 4,
                        lineCap: .butt,
                        lineJoin: .bevel,
                        miterLimit: 1,
                        dash: [],
                        dashPhase: 1
                    )
                )
            }
        }
    }
    

The Charts framework includes _AxisMarks_ type representing the chart’s axes.
We can use it to customize the axis in different ways. In the example above,
we use the example of the _AxisMark_ type, allowing us to configure the axis’s
preset, position, values, and stroke.

The _preset_ parameter provides _automatic, aligned, inset, and extended_
options. They all affect how the framework draws the value on the axis. The
_position_ parameter allows us to choose where to draw axis values. We can use
the _values_ parameter to generate values to draw on the axis. In our example,
we use the _stride_ function to generate values. The last parameter is the
_stroke_ . The framework uses it to draw axis lines.

We can also use another variant of the _AxisMarks_ to fully customize the look
and feel by manually adjusting every axis component per axis value.

    
    
    struct ContentView: View {
        var body: some View {
            Chart {
                // ...
            }
            .chartXAxis {
                AxisMarks(values: .stride(by: 500)) { value in
                    AxisGridLine(
                        centered: true,
                        stroke: StrokeStyle(
                            lineWidth: 4,
                            lineCap: .butt,
                            lineJoin: .bevel,
                            miterLimit: 1,
                            dash: [],
                            dashPhase: 1
                        )
                    )
                    
                    AxisValueLabel(anchor: .topTrailing)
                    
                    if let value = value.as(Int.self), value % 2 == 0 {
                        AxisTick(centered: true, length: 10)
                    }
                }
            }
        }
    }
    

As you can see in the example above, we use another variant of the _AxisMarks_
initializer, allowing us to configure the axis look and feel per value. We use
the concrete value to decide whether to show the tick. The last example
demonstrates how we can use _AxisGridLine_ , _AxisValueLabel_ , and _AxisTick_
types to compose the axis. They provide many customization points, allowing
you to reach the desired look and feel.

I hope you enjoy the post. Feel free to follow me on [ Twitter
](https://twitter.com/mecid) and ask your questions related to this post.
Thanks for reading, and see you next week!

