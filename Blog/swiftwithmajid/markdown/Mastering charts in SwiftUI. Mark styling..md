##  Mastering charts in SwiftUI. Mark styling.

18 Jan 2023

Last week we started a series of posts about the new Charts framework
available on the latest Apple platforms. We talked about basic stuff and
learned how to plot data. This week we will continue mastering the Charts
framework by learning different customization and styling options available.

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

As we learned in the previous post, the Charts framework provides different
mark types, allowing us to plot our data differently. _AreaMark_ , _BarMark_ ,
_LineMark_ , _PointMark_ , _RectangleMark_ , and _RuleMark_ , all of these
mark types let us apply modifiers we used to have in SwiftUI views.

> To learn more about the basics of the Charts framework, take a look at my
> dedicated [ “Mastering charts in SwiftUI. Basics.” ](/2023/01/10/mastering-
> charts-in-swiftui-basics/) post.

For example, we can use the _foregroundStyle_ modifier to change the mark’s
color using any _ShapeStyle_ we need or the _opacity_ modifier to change the
alpha of the mark.

    
    
    enum Gender: String {
        case male
        case female
        case notSet
    }
    
    extension Gender: Plottable {
        var primitivePlottable: String {
            rawValue
        }
    }
    
    struct Stats {
        let city: String
        let population: Int
        let gender: Gender
    }
    
    struct ContentView1: View {
        let stats: [Stats]
        
        var body: some View {
            Chart {
                ForEach(stats, id: \.city) { stat in
                    BarMark(
                        x: .value("City", stat.city),
                        y: .value("Population", stat.population)
                    )
                    .opacity(0.3)
                    .foregroundStyle(.red)
                }
            }
        }
    }
    

> To learn more about the _ShapeStyle_ protocol, take a look at my [ “The many
> faces of ShapeStyle in SwiftUI” ](/2021/11/17/the-many-faces-of-shapestyle-
> in-swiftui/) post.

![chart-with-opacity-and-color](/public/chart10.png)

The _clipShape_ modifier allows us to change the shape of the bar mark, and
the _position_ modifier will enable us to stack bar marks in a group
differently.

    
    
    struct ContentView1: View {
        let stats: [Stats]
        
        var body: some View {
            Chart {
                ForEach(stats, id: \.city) { stat in
                    BarMark(
                        x: .value("City", stat.city),
                        y: .value("Population", stat.population)
                    )
                    .foregroundStyle(by: .value("Gender", stat.gender))
                    .clipShape(RoundedRectangle(cornerRadius: 16))
                    .position(by: .value("Gender", stat.gender))
                }
            }
        }
    }
    

![bar-chart-with-custom-stacking](/public/chart6.png)

As you can see in the example above, we use the _clipShape_ modifier to round
the rectangles of our bars. We also use the _position_ modifier to stack them
horizontally. By default, the Charts framework accumulates bars in a single
group vertically.

On the other hand, the _LineMark_ type allows us to use the _lineStyle_
modifier to change the stroke style of the plotted line. We can also use the
_interpolationMethod_ modifier to change how the framework draws the line.

    
    
    struct ContentView: View {
        let numbers: [Double]
        
        var body: some View {
            Chart {
                RuleMark(y: .value("Limit", 50))
                
                ForEach(Array(numbers.enumerated()), id: \.offset) { index, value in
                    LineMark(
                        x: .value("Index", index),
                        y: .value("Value", value)
                    )
                    .interpolationMethod(.catmullRom)
                    .lineStyle(StrokeStyle(lineWidth: 1, dash: [2]))
                    
                    PointMark(
                        x: .value("Index", index),
                        y: .value("Value", value)
                    )
                }
            }
        }
    }
    

![line-chart-with-custom-curve](/public/chart7.png)

In the example above, we use the _lineStyle_ modifier to provide a custom
stroke style. Here we use particular dash values allowing us to draw the
dashed line. We also apply the _interpolationMethod_ modifier with
_catmullRom_ value to draw a curved line instead of a straight one.

The Charts framework has smart defaults and can extract value from your data
to do some stuff automatically without your notice. For example, it can
understand your data and color it or automatically generate a legend for your
chart.

![chart-with-legend](/public/chart11.png)

One of my favorite things about the new Charts framework is how data
annotating works. You can annotate any mark on your chart with a SwiftUI view.
It means you can plot your data and place SwiftUI views inside your chart
close to your data point.

> To learn more about the logic behind the _ViewBuilder_ type, take a look at
> my [ “The power of @ViewBuilder in SwiftUI” ](/2019/12/18/the-power-of-
> viewbuilder-in-swiftui/) post.

Annotating data points with the new Chart framework is easy. Every mark type
provides us with the _annotation_ modifier accepting a _ViewBuilder_ closure
where we can construct our SwiftUI view.

    
    
    struct ContentView1: View {
        let stats: [Stats]
        
        var body: some View {
            Chart {
                ForEach(stats, id: \.city) { stat in
                    BarMark(
                        x: .value("City", stat.city),
                        y: .value("Population", stat.population)
                    )
                    .clipShape(RoundedRectangle(cornerRadius: 16))
                    .position(by: .value("Gender", stat.gender))
                    .annotation {
                        Text(verbatim: stat.population.formatted())
                            .font(.caption)
                    }
                }
            }
        }
    }
    

![chart-with-annotation](/public/chart8.png)

As you can see in the example above, we use the _annotation_ modifier to place
the text with the population above the bar mark. The _annotation_ modifier
also accepts the _position_ , _alignment_ , and _spacing_ parameters.

    
    
    struct ContentView1: View {
        let stats: [Stats]
        
        var body: some View {
            Chart {
                ForEach(stats, id: \.city) { stat in
                    BarMark(
                        x: .value("City", stat.city),
                        y: .value("Population", stat.population)
                    )
                    .clipShape(RoundedRectangle(cornerRadius: 16))
                    .position(by: .value("Gender", stat.gender))
                    .annotation(position: .bottom, alignment: .trailing, spacing: 16) {
                        Text(verbatim: stat.population.formatted())
                            .font(.caption)
                    }
                }
            }
        }
    }
    

![chart-with-annotation](/public/chart9.png)

We can put an annotation under the bar, above it, or overlay it. Remember that
you can place as many annotations as you need, but try to leave your charts
manageable with annotations.

Today we learned how to style our data points in the new Charts framework. I
hope you enjoy the post. Feel free to follow me on [ Twitter
](https://twitter.com/mecid) and ask your questions related to this post.
Thanks for reading, and see you next week!

