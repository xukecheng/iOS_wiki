##  Mastering charts in SwiftUI. Basics.

10 Jan 2023

Swift Charts is a new framework by Apple allowing us to visualize our data in
a declarative way using SwiftUI. The Swift Charts framework inherits from
SwiftUI its declarative nature and the power of intelligent defaults. This
week we will start with the basics of the Charts framework.

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

Let’s start by plotting a simple line chart from an array of numbers.

    
    
    struct ContentView: View {
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
    

![mastering-chart](/public/chart1.png)

As you can see in the example above, we define an instance of the _Chart_
view. Then inside the _ViewBuilder_ closure of the _Chart_ view, we use the
_ForEach_ view to place the array of numbers using the _LineMark_ . The
_Chart_ view is smart enough to plot the single line passing all the points
defined via _LineMark_ .

> To learn more about the logic behind the _ViewBuilder_ type, take a look at
> my [ “The power of @ViewBuilder in SwiftUI” ](/2019/12/18/the-power-of-
> viewbuilder-in-swiftui/) post.

Swift Charts allow us to compose different types of marks on a single chart.
We have plenty of marks in use, like _AreaMark_ , _BarMark_ , _LineMark_ ,
_PointMark_ , _RectangleMark_ , and _RuleMark_ .

    
    
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
                    
                    PointMark(
                        x: .value("Index", index),
                        y: .value("Value", value)
                    )
                }
            }
        }
    }
    

![mastering-chart](/public/chart2.png)

In the example above, we use the _PointMark_ type to draw a circular point for
every data point. We also use _RuleMark_ to draw a horizontal limit line. As
you can see, we easily compose different marks on the same chart.

The heart of the Swift Charts framework is the _Plottable_ protocol. It allows
us to define a mark with any value that conforms to the _Plottable_ protocol.
By default, types like _Int_ , _String_ , _Double_ , _Date_ , and _Decimal_
conform to the _Plottable_ protocol. But you can always conform your own type
to the _Plottable_ protocol if needed.

Swift Charts support quantitative, categorical, and temporal values. For
example, _Double_ is quantitative, _String_ is categorical, and _Date_ is
temporal value.

    
    
    enum Gender: String {
        case male
        case female
        case notSet
    }
    
    struct Stats {
        let city: String
        let population: Int
        let gender: Gender
    }
    

Here we create a type called _Stats_ to define a city’s population by gender.
The city’s population is a quantitative value. The name and gender are
categorical.

    
    
    struct ContentView1: View {
        let stats: [Stats]
        
        var body: some View {
            Chart {
                ForEach(stats, id: \.city) { stat in
                    BarMark(
                        x: .value("City", stat.city),
                        y: .value("Population", stat.population)
                    )
                }
            }
        }
    }
    
    struct ContentView_Previews: PreviewProvider {
        static var previews: some View {
            NavigationStack {
                ContentView1(
                    stats: [
                        .init(city: "NY", population: 10_164_966, gender: .female),
                        .init(city: "NY", population: 9_581_261, gender: .male),
                        .init(city: "LA", population: 5_133_906, gender: .female),
                        .init(city: "LA", population: 4_982_799, gender: .male)
                    ]
                )
                .preferredColorScheme(.dark)
            }
        }
    }
    

![mastering-chart](/public/chart3.png)

As you can see in the example above, we use the _BarMark_ type to draw the
population of the provided cities. We use the city name, which is categorical
type as X position. That’s why the _Chart_ view concatenate every mark with
the same X position.

    
    
    struct ContentView1: View {
        let stats: [Stats]
        
        var body: some View {
            Chart {
                ForEach(stats, id: \.city) { stat in
                    BarMark(
                        x: .value("City", stat.city),
                        y: .value("Population", stat.population)
                    )
                    .foregroundStyle(by: .value("Gender", stat.gender.rawValue))
                }
            }
        }
    }
    

![mastering-chart](/public/chart4.png)

We can use different foreground styles for the _BarMark_ type and style them
using gender value. It allows us to see the different ranges in a single bar.

    
    
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
                    .foregroundStyle(by: .value("Gender", stat.gender))
                }
            }
        }
    }
    

Now we conform the _Gender_ type to the _Plottable_ protocol to simplify our
code a little bit. Remember that you can provide any logic you need to convert
your custom data to plottable primitives.

Today we learned basics of the new Swift Charts framework. Charts framework
provides us a lot of defaults out of the box. Every chart we build supports
accessibility and automatically provides us legends, correctly scaled plotting
area, etc.

In the next posts, we will learn more about customization options in the new
Charts framework. I hope you enjoy the post. Feel free to follow me on [
Twitter ](https://twitter.com/mecid) and ask your questions related to this
post. Thanks for reading, and see you next week!

