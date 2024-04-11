##  Sharing content in SwiftUI

28 Mar 2023

Apple introduced a brand new CoreTransferable framework and _ShareLink_ view
in SwiftUI, allowing us to share and export content from our apps very
declaratively. This week we will learn how to make data transferable and use
the new _ShareLink_ view in SwiftUI.

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

####  ShareLink

The new _ShareLink_ looks like a plain button but integrates the share sheet
and exports data in the provided format. Let’s look at the simple example of
using the _ShareLink_ view in SwiftUI.

    
    
    struct Food: Codable {
        var title: String
        var ingredients: [String]
    }
    
    struct ContentView: View {
        @State private var food = Food(title: "", ingredients: [])
        
        var body: some View {
            Form {
                Section {
                    TextField("title", text: $food.title)
                }
                
                Section {
                    ForEach($food.ingredients, id: \.self) { $item in
                        TextField("item", text: $item)
                    }
                    
                    Button("Add") {
                        food.ingredients.append("")
                    }
                    
                    ShareLink(
                        "Export",
                        item: food.ingredients.joined(separator: ","),
                        preview: SharePreview("Export \(food.title)")
                    )
                }
            }
        }
    }
    

As you can see in the example above, we have the _Food_ struct containing a
title and an array of ingredients. There is a form allowing us to populate the
instance of the _Food_ type with data. At the bottom of the form, we have an
instance of the _ShareLink_ view that exports the content of the food to a
plain string by joining ingredients. The code above is simple but handles a
share sheet presentation and data export.

But what about other data types like images, binary data, or any other custom
format? All the magic here is hidden behind _ShareLink’s_ **item** parameter.
It works with any type conforming to the _Transferable_ protocol. _String_ ,
_Data_ , and many other types conform to the _Transferable_ protocol out of
the box, and you don’t need to do anything to share them.

####  Transferable

Now we know how the _ShareLink_ view works in SwiftUI. It relies on the
_Transferable_ protocol from the CoreTransferable framework. But what if we
want to share our custom type? In this case, we must conform our type to the
_Transferable_ protocol.

    
    
    import CoreTransferable
    
    extension Food: Transferable {
        static var transferRepresentation: some TransferRepresentation {
            CodableRepresentation(contentType: .text)
        }
    }
    

The _Transferable_ protocol is simple and has the only requirement. We must
implement the _transferRepresentation_ property and return some instance of
the _TransferRepresentation_ type. The framework provides ready-to-use
representation types: _CodableRepresentation_ , _DataRepresentation_ ,
_FileRepresentation_ , and _ProxyRepresentation_ .

In the example above, we use the _CodableRepresentation_ because our _Food_
type conforms to the _Codable_ protocol. This conformance allows us to
automatically export any instance of the Food type as a JSON string.

We also can use _DataRepresentation_ if you can convert your value type into
an instance of the _Data_ type, or we can use _FileRepresentation_ whenever
the value represents a file on the disk.

    
    
    import CoreTransferable
    import UniformTypeIdentifiers
    
    extension UTType {
        static var food: UTType {
            UTType(exportedAs: "myapp.food.type")
        }
    }
    
    extension Food: Transferable {
        static var transferRepresentation: some TransferRepresentation {
            CodableRepresentation(contentType: .food)
            CodableRepresentation(contentType: .text)
        }
    }
    

The _transferRepresentation_ property is marked with the
_TransferRepresentationBuilder_ and allows us to combine different
representations. For example, you can define different representations for
different content types. Remember, the order makes sense; you should keep the
most important representations above others.

Today we learned about the new CoreTransferable framework and how to use the
_ShareLink_ view in SwiftUI. The CoreTransferable framework plays a massive
role in exporting your data from the app. But it works also behind the drag
and drop, and I will cover this part next week.

I hope you enjoy the post. Feel free to follow me on [ Twitter
](https://twitter.com/mecid) and ask your questions related to this post.
Thanks for reading, and see you next week!

