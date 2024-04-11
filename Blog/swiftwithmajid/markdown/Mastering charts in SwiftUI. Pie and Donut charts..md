##  Mastering charts in SwiftUI. Pie and Donut charts.

26 Sep 2023

One of the additions to the Swift Charts framework after WWDC 23 was a brand
new _SectorMark_ type. The _SectorMark_ allows us to build pie and donut
charts in SwiftUI easily. This week, we will learn how to plot the data using
_SectorMark_ .

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

The Swift Charts framework provides us with mark types like _BarMark_ ,
_LineMark_ , etc. Mark types allow us to define a piece of data on the chart
declaratively. _SectorMark_ is another mark type we can use to plot a pie or
donut chart.

    
    
    import SwiftUI
    import Charts
    
    struct Product: Identifiable {
        let id = UUID()
        let title: String
        let revenue: Double
    }
    
    struct SectorChartExample: View {
        @State private var products: [Product] = [
            .init(title: "Annual", revenue: 0.7),
            .init(title: "Monthly", revenue: 0.2),
            .init(title: "Lifetime", revenue: 0.1)
        ]
        
        var body: some View {
            Chart(products) { product in
                SectorMark(
                    angle: .value(
                        Text(verbatim: product.title),
                        product.revenue
                    )
                )
                .foregroundStyle(
                    by: .value(
                        Text(verbatim: product.title),
                        product.title
                    )
                )
            }
        }
    }
    

![pie-chart](/public/pie.png)

As you can see in the example above, we use the _SectorMark_ type to plot a
pie chart. We use the _foregroundStyle_ modifier to fill sections with
different colors as we do with other mark types.

> To learn more about mark styling, take a look at my dedicated [ “Mastering
> charts in SwiftUI. Mark styling.” ](/2023/01/18/mastering-charts-in-swiftui-
> mark-styling/) post.

Whenever we create an instance of the _SectorMark_ type, we must pass the
_angle_ parameter. It might be a plottable value defining an angle portion of
the section, or we can pass a range with exact start and end values of the
angle for a particular area.

The second parameter of the _SectorMark_ initializer is the _innerRadius_
value. We can use it to transform our pie chart into a donut chart.

    
    
    struct SectorChartExample: View {
        @State private var products: [Product] = [
            .init(title: "Annual", revenue: 0.7),
            .init(title: "Monthly", revenue: 0.2),
            .init(title: "Lifetime", revenue: 0.1)
        ]
        
        var body: some View {
            Chart(products) { product in
                SectorMark(
                    angle: .value(
                        Text(verbatim: product.title),
                        product.revenue
                    ),
                    innerRadius: .ratio(0.6)
                )
                .foregroundStyle(
                    by: .value(
                        Text(verbatim: product.title),
                        product.title
                    )
                )
            }
        }
    }
    

![donut-chart](/public/donut.png)

As you can see in the example above, we use the _innerRadius_ parameter to
plot a donut chart. The _innerRadius_ parameter accepts _ratio_ , _inset_ ,
and _fixed_ sizes. We can use the _angularInset_ parameter to set the spacing
between sectors of the pie or donut charts.

    
    
    struct SectorChartExample: View {
        @State private var products: [Product] = [
            .init(title: "Annual", revenue: 0.7),
            .init(title: "Monthly", revenue: 0.2),
            .init(title: "Lifetime", revenue: 0.1)
        ]
        
        var body: some View {
            Chart(products) { product in
                SectorMark(
                    angle: .value(
                        Text(verbatim: product.title),
                        product.revenue
                    ),
                    innerRadius: .ratio(0.6),
                    angularInset: 8
                )
                .foregroundStyle(
                    by: .value(
                        Text(verbatim: product.title),
                        product.title
                    )
                )
            }
        }
    }
    

![donut-chart-with-spacing](/public/donut1.png)

As you can see, the _SectorMark_ type is a simple chart mark that supports all
the modifiers we use for other mark types to customize them. I hope you enjoy
the post. Feel free to follow me on [ Twitter ](https://twitter.com/mecid) and
ask your questions related to this post. Thanks for reading, and see you next
week!

