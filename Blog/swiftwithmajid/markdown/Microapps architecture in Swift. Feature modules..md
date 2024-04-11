##  Microapps architecture in Swift. Feature modules.

19 Jan 2022

In the first post of the current series, I talked about Swift Package Manager
basics and how we can maintain the project with many Swift modules. This week
we continue the topic of Microapps architecture by introducing feature
modules.

**Enhancing the Xcode Simulators.**  
Compare designs, show rulers, add a grid, quick actions for recent builds.
Create recordings with touches & audio, trim and export them into MP4 or GIF
and share them anywhere using drag & drop. Add bezels to screenshots and
videos. [ Try now ](https://gumroad.com/a/931293139/ftvbh)

[ Last week ](/2022/01/12/microapps-architecture-in-swift-spm-basics/) we
created a separate module for the design system of our app that contains
buttons and other shared UI components. We call them foundation modules
because we will import them into many different modules and use their
functionality. Another excellent example of the foundation module is the
networking layer. We can also extract it into a separate module and import it
whenever needed.

In the current post, I want to focus on the feature modules. Feature module
provides complete functionality for a dedicated app feature. We can also call
them product modules because they usually implement a particular part of the
final product. Let’s create the first feature module that onboards users on
the first app launch. As always, we should start with declaring our module in
the _Package.swift_ file.

    
    
    import PackageDescription
    
    let package = Package(
        name: "MyAppLibrary",
        platforms: [.iOS(.v15)],
        products: [
            .library(name: "DesignSystem", targets: ["DesignSystem"]),
            .library(name: "Onboarding", targets: ["Onboarding"])
        ],
        dependencies: [],
        targets: [
            .target(name: "DesignSystem"),
            .testTarget(
                name: "DesignSystemTests",
                dependencies: ["DesignSystem"]
            ),
            .target(
                name: "Onboarding",
                dependencies: ["DesignSystem"]
            )
        ]
    )
    

As you can see, we define the _Onboarding_ module as a separate target with
_DesignSystem_ as the dependency. It allows us to import the _DesignSystem_
module and reuse its functionality. The onboarding screen should present a few
items that we define below.

    
    
    public struct OnboardingItem: Hashable {
        let systemImage: String
        let title: String
        let body: String
    
        public init(
            systemImage: String,
            title: String,
            body: String
        ) {
            self.systemImage = systemImage
            self.title = title
            self.body = body
        }
    }
    

Please look at how we use the _public_ access modifier to make the dedicated
parts of code visible outside of the current module. Now we can move to
_OnboardingView_ itself.

    
    
    import DesignSystem
    
    public struct OnboardingView: View {
        let items: [OnboardingItem]
        let action: () -> Void
    
        public init(
            items: [OnboardingItem],
            action: @escaping () -> Void
        ) {
            self.items = items
            self.action = action
        }
    
        public var body: some View {
            VStack(alignment: .leading, spacing: 16) {
                Spacer()
                ForEach(items, id: \.self) { item in
                    HStack {
                        Image(systemName: item.systemImage)
                            .resizable()
                            .frame(width: 48, height: 48)
                        VStack(alignment: .leading) {
                            Text(item.title)
                                .font(.headline)
                            Text(item.body)
                                .foregroundColor(.secondary)
                        }
                    }
                }
    
                Button("Start using app", action: action)
                    .buttonStyle(.main)
                    .padding(.vertical)
                Spacer()
            }
        }
    }
    

First, we import the _DesignSystem_ module to use the main button style. Next,
we implement the _OnboardingView_ by iterating through onboarding items and
presenting them in the vertical stack. We also display a button on the bottom
of the screen with the style that we imported from the _DesignSystem_ module.

OK, now we have a separate module representing the onboarding feature.
Remember that we should implement all the app logic in the dedicated feature
modules. The app target should only provide a thin coordinator layer that
instantiates different features and navigates between them.

    
    
    import SwiftUI
    import Onboarding
    import DailySummary
    
    struct RootView: View {
        @AppStorage("isFirstLaunch")
        var isFirstLaunch: Bool = true
    
        var body: some View {
            NavigationView {
                DailySummaryView(date: .now)
            }
            .sheet(isPresented: $isFirstLaunch) {
                OnboardingView(
                    items: [
                        .init(
                            systemImage: "pills",
                            title: "Pills",
                            body: "Track your pills"
                        ),
                        .init(
                            systemImage: "heart",
                            title: "Monitor",
                            body: "Monitor your heart"
                        )
                    ]
                ) {
                    isFirstLaunch = false
                }
            }
        }
    }
    

As you can see in the example above, we have the _RootView_ in the app target
that imports both _Onboarding_ and _DailySummary_ modules. _RootView_ doesn’t
contain any logic. The only thing it does is coordinate between two feature
modules.

Dividing the app into many decoupled feature modules allows us to create
micro-apps for different user flows and deliver them to the QA team to get
early feedback without waiting for other features.

Feature modules can contain more than one screen and should encapsulate the
whole feature. For example, it can be a multi-screen checkout feature in the
store app. A dedicated team can work on this module and deliver a microapp
using TestFlight to test the checkout flow.

This week we learned about the feature modules and how they can improve the
development of the big app by delivering a microapp for the dedicated feature
set. I hope you enjoy the post. Feel free to follow me on [ Twitter
](https://twitter.com/mecid) and ask your questions related to this post.
Thanks for reading, and see you next week!

####  References

  1. [ Meet the microapps architecture ](https://increment.com/mobile/microapps-architecture/)
  2. [ Introduction to App Modularisation with Swift Package Manager ](https://holyswift.app/introduction-to-app-modularisation-with-swift-package-manager-a-tale-to-be-told)

