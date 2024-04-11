##  Microapps architecture in Swift. Resources and localization.

26 Jan 2022

This week we will continue the topic of microapps architecture in Swift by
touching on another essential edge of this approach. In this post, we will
talk about sharing resources between modules and separating the localization
of feature modules.

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

####  Bundle API

Usually, we don’t care much about resource bundles in single module apps
because the only bundle is the app target bundle. Let’s take a quick look at
the example using Bundle API.

    
    
    Image("image")
    Image("image", bundle: nil)
    Image("image", bundle: .main)
    

These three lines do the same thing. They look for the image in the bundle of
the running target. We can try to access an image from a particular bundle.
Here is another example.

    
    
    Image("image", bundle: Bundle(identifier: "com.example.myapp"))
    

####  SPM and Resources

Swift Package Manager allows us to put code and related resources in Swift
modules. In this case, the Swift compiler generates a bundle for every module
that contains resources. Imagine our design system module containing an asset
catalog with custom icons to reuse in feature modules.

To achieve that, first, we need to create an asset catalog with icons and
place it inside the _DesignSystem_ folder. Xcode automatically recognizes the
format of the asset catalog and generates a bundle for the module. You can
access the bundle of the current module by using the **module** property on
the _Bundle_ type. But remember, Xcode generates it only for modules with
resources inside.

    
    
    // DesignSystem module
    extension UIImage {
        public enum Icon: String {
            case trash
            case star
            case plus
        }
    
        public static func get(_ icon: Icon) -> UIImage {
            .init(
                named: icon.rawValue,
                in: .module,
                compatibleWith: .current
            )!
        }
    }
    

As you can see in the example above, we create a type-safe image factory that
loads icons from the design system bundle. Please look at how we use the
_module_ property on the _Bundle_ type. This is how we can load the resources
from the bundle of the current module. If we omit the _bundle_ parameter, the
app will try to load the image from the app target module, which doesn’t
contain these images.

> To learn more about writing type-safe code in Swift, take a look at my [
> “Writing idiomatic Swift code” ](/2021/04/01/writing-idiomatic-swift-code/)
> post.

Xcode automatically generates bundles whenever finds asset catalogs, Core Data
models, Storyboards, NIBs, and localization files. For any other types of
resources, you should use _Package.swift_ file to ask the Swift compiler to
bundle them.

    
    
    // Package.swift
    let package = Package(
        ...
        targets: [
            .target(
                name: "DesignSystem",
                dependencies: [],
                resources: [
                    .copy("Resources/Fonts"),
                    .process("Resources/PNGs")
                ]
            )
        ]
    )
    

The design system module contains the _Resources_ folder with fonts and
different PNGs that I want to bundle with my module. Unfortunately, Xcode
doesn’t recognize them automatically, but we can bundle them manually via a
few lines of code in the _Package.swift_ file. There are two ways of bundling
resources in Swift modules. We can process or copy them directly in the
bundle.

When you choose processing resources, Xcode applies platform-specific rules
for compressing files, when you select copying, Xcode copies files simply by
keeping the structure of the sub-directories.

####  SPM and Localization

Swift Packages support localization out of the box. Every feature module
should contain its localization file and be ready to build and run as a
separate microapp. We can quickly achieve that by enabling localization in the
_Package.swift_ file by adding a single line of code.

    
    
    // Package.swift
    let package = Package(
        name: "MyAppLibrary",
        defaultLocalization: "en",
        platforms: [.iOS(.v15)],
        ...
    )
    

We added the _defaultLocalization_ parameter to the package declaration in the
example above. This parameter is necessary if you want to support
localization. Now you can create _en.lproj, es.lproj, or any-locale-
identifier.lproj_ folders in your module to place your _Localizable.strings_
files with particular translations. Remember that you still need to specify
the correct bundle whenever you want to access the localization of the current
module.

    
    
    // Feature module
    Text("helloMessage", bundle: .module)
    

We should learn from SwiftUI views how to leverage the power of modules while
modeling the public interfaces of our custom views. For example, the design
system module contains a generic view that I use as an empty or error view. I
will use it in various feature modules with different localizations coming
from different bundles.

    
    
    // DesignSystem module
    public struct PlaceholderView: View {
        let systemImage: String
        let text: LocalizedStringKey
        let bundle: Bundle?
    
        public init(
            _ text: LocalizedStringKey,
            bundle: Bundle? = nil,
            systemImage: String
        ) {
            self.systemImage = systemImage
            self.bundle = bundle
            self.text = text
        }
    
        public var body: some View {
            Label {
                Text(text, bundle: bundle)
                    .multilineTextAlignment(.center)
            } icon: {
                Image(systemName: systemImage)
                    .imageScale(.large)
                    .font(.largeTitle)
            }
            .labelStyle(.vertical)
            .padding(.horizontal)
            .padding(.horizontal)
        }
    }
    

As you can see in the example above, we define a public _init_ that accepts
the bundle to retrieve localization. Without this parameter, the view can
access only the main or its own bundle. But we need to access bundles of
various feature modules. That’s why we have to introduce an optional _bundle_
parameter.

    
    
    // Search feature module
    import DesignSystem
    
    struct SearchView: View {
        let results: [SearchItems]
        
        var body: some View {
            if results.isEmpty {
                PlaceholderView(
                    "emptySearchPlaceholder",
                    bundle: .module,
                    systemImage: "magnifyingglass"
                )
            } else {
            // display the list of items
            }
        }
    }
    

####  Conclusion

This week we learned how to use resources within microapps architecture. We
also learned how to encapsulate localization inside the feature modules. There
are two rules which I use to build well-separated modules.

First, I try to keep resources only inside the module that uses them. Feature
modules contain the localization strings they need. Second, create a type-safe
public API for retrieving shared resources, as we do in the design system
module, to get the icons across different feature modules.

I hope you enjoy the post. Feel free to follow me on [ Twitter
](https://twitter.com/mecid) and ask your questions related to this post.
Thanks for reading, and see you next week!

####  References

  1. [ Meet the microapps architecture ](https://increment.com/mobile/microapps-architecture/)
  2. [ Introduction to App Modularisation with Swift Package Manager ](https://holyswift.app/introduction-to-app-modularisation-with-swift-package-manager-a-tale-to-be-told)
