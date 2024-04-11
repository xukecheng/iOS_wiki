在本文中，我们将对 `@UIApplicationDelegateAdaptor` 、 `@AccessibilityFocusState` 、 `@FocusedObject` 、 `@FocusedValue` 和 `@FocusedBinding`
等属性包装器进行探讨。这些属性包装器涵盖了不同框架声明周期的整合、辅助聚焦、焦点值观察管理等功能。

> 本文旨在提供对这些属性包装器的主要功能和使用注意事项的概述，而非详尽的使用指南。

- [ @State、@Binding、@StateObject、@ObservedObject、@EnvironmentObject、@Environment ](/zh/posts/exploring-key-property-wrappers-in-swiftui/)
- [ @AppStorage、@SceneStorage、@FocusState、@GestureState、@ScaledMetric ](/zh/posts/exploring-swiftui-property-wrappers-2/)
- [ @FetchRequest、@SectionedFetchRequest、@Query、@Namespace、@Bindable ](/zh/posts/exploring-swiftui-property-wrappers-3/)

## 1\. @UIApplicationDelegateAdaptor

`@UIApplicationDelegateAdaptor` 为开发者提供了在以 SwiftUI 生命周期为基础的应用中访问和利用 UIKit 的
AppDelegate 功能的能力，从而处理如推送通知、生命周期事件等 UIKit 特有的任务。

### 1.1 基本用法

    class AppDelegate: NSObject,UIApplicationDelegate {
        // 实现相关的 UIApplicationDelegate 方法
        func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey : Any]? = nil) -> Bool {
                print("App launched")
                return true
            }
    }

    @main
    struct DelegateDemo: App {
        @UIApplicationDelegateAdaptor var delegate:AppDelegate
        var body: some Scene {
            WindowGroup {
                ContentView()
            }
        }
    }

在上述代码示例中，我们首先声明了一个同时遵循 `NSObject` 和 `UIApplicationDelegate` 协议的类。接着，通过使用 `UIApplicationDelegateAdaptor` ，我们在 App 的声明中对这个类进行了注册。

### 1.2 主要功能

- 允许 SwiftUI 应用利用 UIKit 提供的丰富功能，如后台任务处理、App 生命周期管理等。
- 对于现有的 UIKit 应用，使用 `@UIApplicationDelegateAdaptor` 可以更平滑地过渡到 SwiftUI，而无需重写大量的应用逻辑。

### 1.3 注意事项与使用技巧

- **唯一性与位置限制：** `UIApplicationDelegateAdaptor` 应在 App 的主体声明中定义，并且在整个应用中只能定义一次。
- **环境变量注入：** 处理 AppDelegate 逻辑的类可以实现 `ObservableObject` 协议，并通过环境变量注入到视图树中。这样，可以在视图内部使用 `@EnvironmentObject` 获取 AppDelegate 的实例。

  class AppDelegate: NSObject,UIApplicationDelegate,ObservableObject {
  @Published var launched:Bool = false
  func application(\_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey : Any]? = nil) -> Bool {
  launched = true
  return true
  }
  }

  @main
  struct DelegateDemo: App {
  @UIApplicationDelegateAdaptor var delegate:AppDelegate
  var body: some Scene {
  WindowGroup {
  ContentView()
  .environmentObject(delegate)
  }
  }
  }

  struct ContentView:View {
  @EnvironmentObject var delegate:AppDelegate
  var body: some View {
  Text("Launched \(delegate.launched ? "True" : "False")")
  }
  }

- **聚焦生命周期与系统事件：** `AppDelegate` 类建议专注于应用生命周期和系统事件的处理，避免混入业务逻辑。
- **处理 SceneDelegate 事件：** 若要响应 `UIWindowSceneDelegate` 的事件，可以按以下方式实现：

  final class SceneDelegate:NSObject,UIWindowSceneDelegate{
  func sceneWillEnterForeground(\_ scene: UIScene) {
  print("will enter foreground")
  }
  }

  extension AppDelegate {
  func application(\_ application: UIApplication,
  configurationForConnecting connectingSceneSession: UISceneSession,
  options: UIScene.ConnectionOptions) -> UISceneConfiguration {
  let sceneConfig = UISceneConfiguration(name: nil, sessionRole: connectingSceneSession.role)
  sceneConfig.delegateClass = SceneDelegate.self
  return sceneConfig
  }
  }

- **自动注入 SceneDelegate：** 如果 `SceneDelegate` 实现了 `ObservableObject` ，并且 `AppDelegate` 被注入环境中，SwiftUI 也会自动将 `SceneDelegate` 注入相同环境。

  extension SceneDelegate:ObservableObject {}

  ContentView()
  .environmentObject(delegate)

  struct ContentView1:View {
  @EnvironmentObject var appDelegate:AppDelegate
  @EnvironmentObject var sceneDelegate:SceneDelegate
  var body: some View {
  Text("Launched \(appDelegate.launched ? "True" : "False")")
  }
  }

- **Observation 框架适用性：** 上述逻辑在使用 Observation 框架时同样适用。

  @Observable // Using Observation
  class AppDelegate: NSObject,UIApplicationDelegate {
  var launched:Bool = false
  func application(\_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey : Any]? = nil) -> Bool {
  launched = true
  print("lanched")
  return true
  }
  }

  @Observable // Using Observation
  final class SceneDelegate:NSObject,UIWindowSceneDelegate{
  var foreground:Bool = false
  func sceneWillEnterForeground(\_ scene: UIScene) {
  foreground = true
  print("will enter foreground")
  }
  }

  extension AppDelegate {
  func application(\_ application: UIApplication,
  configurationForConnecting connectingSceneSession: UISceneSession,
  options: UIScene.ConnectionOptions) -> UISceneConfiguration {
  let sceneConfig = UISceneConfiguration(name: nil, sessionRole: connectingSceneSession.role)
  sceneConfig.delegateClass = SceneDelegate.self
  return sceneConfig
  }
  }

  @main
  struct PropertyWrapperApp: App {
  @UIApplicationDelegateAdaptor(AppDelegate.self) var delegate
  var body: some Scene {
  WindowGroup {
  ContentView1()
  .environment(delegate) // 按照 Observed 的方式注入
  }
  }
  }

  struct ContentView1:View {
  @Environment(AppDelegate.self) var appDelegate
  @Environment(SceneDelegate.self) var sceneDelegate
  var body: some View {
  VStack {
  Text("Launched \(appDelegate.launched ? "True" : "False")")
  Text("Foreground \(sceneDelegate.foreground ? "True" : "False")")
  }
  }
  }

- **优先使用 SwiftUI 原生事件处理：** 对于 SwiftUI 已提供原生支持的事件处理逻辑，如 `sceneWillEnterForeground` ，建议优先使用原生方法，例如响应 `scenePhase` 环境值。

  struct ContentView:View {
  @Environment(\.scenePhase) var scenePhase
  var body: some View {
  Text("Hello World")
  .onChange(of: scenePhase){ phase in
  switch phase {
  case .active: // 对应 sceneWillEnterForeground
  print("active")
  case .inactive:
  print("inactive")
  case .background:
  print("background")
  @unknown default:
  break
  }
  }
  }
  }

- **其他原生修饰器：**SwiftUI 还提供了一系列修饰器，可以用来避免在 Delegate 中处理某些事件，如 `onContinueUserActivity` 、 `backgroundTask` 、 `handlesExternalEvents` 、 `onOpenURL` 和 `userActivity` 等。在可能的情况下，应优先考虑使用这些 SwiftUI 原生的方法。

> [ `@NSApplicationDelegateAdaptor` > ](https://developer.apple.com/documentation/swiftui/nsapplicationdelegateadaptor)
> 、 [ `@WKApplicationDelegateAdaptor` > ](https://developer.apple.com/documentation/swiftui/wkapplicationdelegateadaptor)
> 和 [ `@WKExtensionDelegateAdaptor` > ](https://developer.apple.com/documentation/swiftui/wkextensiondelegateadaptor)
> 在用法上与 `@UIApplicationDelegateAdaptor`
> 非常相似，但它们分别适配不同的平台。由于这些属性包装器的基本原理相同，本文将不对它们进行单独的讨论。

## 2 @AccessibilityFocusState

`@AccessibilityFocusState` 在 SwiftUI 中被设计用于增强无障碍体验。这个属性包装器使得开发者能够更有效地管理和响应
VoiceOver 等辅助功能的焦点状态，进而为所有用户打造出更加易于导航和操作的应用界面。它在基本概念和应用方法上与 `@FocusState`
非常相似，可以被视为专门针对辅助功能元素的 `@FocusState` 。

### 2.1 基本用法

    // 方式一：
    struct AccessibilityFocusStateView:View {
        @AccessibilityFocusState(for: .switchControl) var isClickButtonFocused:Bool
        var body: some View {
            VStack {
                Button("Press me"){
                    print("Press")
                }

                Button("Click me"){
                    print("Click")
                }
                .accessibilityFocused($isClickButtonFocused)
            }
            .onChange(of: isClickButtonFocused){
                print(isClickButtonFocused)
            }
        }
    }

    // 方式二：
    struct AccessibilityFocusStateView: View {
        @AccessibilityFocusState var focused: FocusField?
        var body: some View {
            VStack {
                Button("Press me") {
                    // do something
                    // then change focus
                    focused = .click
                }
                .accessibilityFocused($focused, equals: .press)

                Button("Click me") {
                    print("Click")
                }
                .accessibilityFocused($focused, equals: .click)
            }
        }
    }

    enum FocusField: Hashable {
        case press
        case click
    }

### 2.2 注意事项与使用技巧

- **特定辅助模式配置：** `@AccessibilityFocusState` 可以根据需要配置，以仅在特定辅助模式下激活，例如 `.switchControl` 或 `.voiceOver` 。默认情况下，它支持所有辅助功能。

  @AccessibilityFocusState(for:.switchControl) var focused: FocusField?
  // or
  @AccessibilityFocusState(for:.voiceOver) var focused: FocusField?

- **无障碍测试：** 为了确保无障碍用户的良好体验，应使用 VoiceOver 等辅助工具测试应用中的焦点管理功能，确保它们按预期运作。
- **避免复杂化：** 在使用 `@AccessibilityFocusState` 时，应避免在不必要的场景中引入过于复杂的焦点管理逻辑，以免造成用户的困扰或混乱。

## 3 @FocusedObject

`@FocusedObject` 用于观察由当前聚焦的视图或场景提供的可观察类型数据。这些数据可以由获得焦点的可观察视图（使用 `.focusedObject` 修饰符）或获得焦点的场景（使用 `.focusedSceneObject` 修饰符）来提供和管理。

### 3.1 基本用法

- **观察聚焦场景数据** ：下面的代码将在 macOS 上创建一个菜单项 Empty，点击它会情况当前聚焦场景中的文本框内容（ 使用 ⌘-N 可以创建新的场景 ）：

  // 要求符合 ObservableObject 协议
  class DataModel:ObservableObject {
  @Published var text = ""
  }

  struct MyCommands:Commands {
  // 获取由当前聚焦场景中，由 focusedSceneObject 提供的 DataModel 实例，如果没有则为 nil
  @FocusedObject var dataModel:DataModel?
  var body: some Commands {
  CommandMenu("Action") {
  Button("Empty"){
  dataModel?.text = ""
  }
  }
  }
  }

  @main
  struct FocusedSceneObjectDemoApp: App {
  var body: some Scene {
  WindowGroup {
  ContentView()
  .scenePadding()
  }
  .commands {
  MyCommands()
  }
  }
  }

  struct ContentView: View {
  @StateObject var dataModel = DataModel()
  var body: some View {
  VStack {
  // focusedSceneObject 在场景聚焦时便会自动提供数据，与当前视图是否可聚焦无关
  Text("Input:")
  .focusedSceneObject(dataModel)
  TextEditor(text: $dataModel.text)
  }
  }
  }

- **观察聚焦视图（ 可聚焦视图 ）数据** ：下面的代码提供与上面代码相同的功能，唯一的区别是 `focusedObject` 需要使用在可聚焦视图或元素上，且只有当该视图或元素获得了焦点后，才会提供数据。

  // 其他代码一样
  struct ContentView: View {
  @StateObject var dataModel = DataModel()
  var body: some View {
  VStack {
  Text("Input:")
  // 由可聚焦视图在获得焦点时提供数据
  TextEditor(text: $dataModel.text)
  .focusedObject(dataModel)
  }
  }
  }

### 3.2 主要功能

`@FocusedObject`
为应用提供了从当前聚焦元素获取可观察对象的能力，这极大地方便了开发者创建动态且响应用户操作的界面。它经常被用于实现需要根据当前焦点状态进行相应处理的功能，如菜单和
HUB 等场景。

### 3.3 注意事项与使用技巧

- **可选值类型：** `@FocusedObject` 应声明为可选（Optional）类型。当相关的焦点场景或元素失去焦点后，该对象的值将自动变为 nil。
- **遵循`ObservableObject` ： ** 用于 `@FocusedObject` 的数据类型必须实现 `ObservableObject` 协议。
- **唯一实例数据：** 类似于 `EnvironmentObject` ，对于任意给定类型，系统在同一时间内仅保留一个实例的数据。因此，应避免同时使用多个 `focusedObject` 或 `focusedSceneObject` 提供同一类型的多份数据。
- **多场景数据提供：** 在多场景应用中，建议使用 `focusedSceneObject` 来提供跨场景数据。
- **使元素可聚焦：** 可以通过 `focusable` 修饰符使原本不可聚焦的元素成为可聚焦的，这样一来，当元素获得焦点时，它也能通过 `focusedObject` 提供数据。

  Text("Input:")
  .focusable()
  .focusedObject(dataModel)

- **观察范围取决于声明位置：** `@FocusedObject` 观察到的数据受其声明位置的影响。在 App 或 Commands 层级声明时，它能够访问所有场景中通过 `focusedObject` 或 `focusedSceneObject` 提供的同类型数据。然而，若在特定场景的代码中声明，则仅能够访问当前场景内由任意视图提供的同类型 `focusedObject` 或 `focusedSceneObject` 数据。

  struct MyCommands: Commands {
  // 可以观察所有场景中的 DataModel 可聚焦数据
  @FocusedObject var dataModel: DataModel?
  var body: some Commands {
  ....
  }
  }

  @main
  struct FocusedSceneObjectDemoApp: App {
  // 可以观察所有场景中的 DataModel 可聚焦数据
  @FocusedObject var dataModel: DataModel?
  var body: some Scene {
  ....
  }
  }

  struct ContentView: View {
  // 仅观察当前场景中的 DataModel 可聚焦数据
  @FocusedObject var dataModel: DataModel?
  var body: some View {
  ....
  }
  }

- **自动识别可聚焦元素：** 除了被直接应用于具体的可聚焦元素， `@FocusedObject` 还能自动识别视图中的所有可聚焦元素。在下面的示例中，无论哪个 `TextEditor` 获得焦点， `@FocusedObject` 都将提供相应的数据：

  VStack {
  TextEditor(text: $dataModel.text)
  TextEditor(text: $dataModel.text2)
  }
  .focusedObject(dataModel)

- **单场景内的多重聚焦：** `@FocusedObject` 不仅适用于跨多个场景的数据观察，也可以在单个场景内发挥作用。例如，下面的代码演示了如何在同一个界面中同时管理用户和产品的不同聚焦状态。

  struct MultiFocusedDemo:View {
  @StateObject var user = UserProfile()
  @StateObject var product = ProductDetails()

      var body: some View {
          Form {
              UserView()
              ProductView()
              Group {
                  TextField("User Name:",text:$user.username)
                  TextField(value: $user.age, format: .number){ Text("Age:")}
              }
              .focusedObject(user)

              Group{
                  TextField("Product Name:",text:$product.productName)
                  TextField(value: $product.price, format: .number){ Text("Price:")}
              }
              .focusedObject(product)

          }
      }

  }

  class UserProfile: ObservableObject {
  @Published var username: String = "JohnDoe"
  @Published var age: Int = 30
  }

  class ProductDetails: ObservableObject {
  @Published var productName: String = "Widget"
  @Published var price: Double = 19.99
  }

  struct UserView: View {
  @FocusedObject var user: UserProfile?

      var body: some View {
          if let userProfile = user {
              Text("Username: \(userProfile.username)")
              Text("Age: \(userProfile.age)")
          }
      }

  }

  struct ProductView: View {
  @FocusedObject var product: ProductDetails?

      var body: some View {
          if let productDetails = product {
              Text("Product: \(productDetails.productName)")
              Text("Price: $\(productDetails.price)")
          }
      }

  }

- **结合其他焦点管理方案：** `@FocusedObject` 可以与其他焦点管理工具结合使用，从而实现更加灵活的交互设计。例如，在下面的代码中，我们通过 `@FocusState` 实现了在元素获得焦点的同时立即获取其相关的可观察对象数据：

  struct FocusStateDemo:View {
  @FocusState var focused:Bool
  @FocusedObject var data:DataModel?
  @StateObject var model = DataModel()
  var body: some View {
  VStack {
  if let text = data?.text {
  Text(text)
  }
  TextField("",text:$model.text)
                    .focused($focused)
  .focusedObject(model)
  }
  .task {
  focused = true
  }
  }
  }

## 4 @FocusedValue

`@FocusedValue` 属性包装器在 SwiftUI 中的作用与 `@FocusedObject` 非常相似，但它专注于值类型及基于
Observation 框架构建的可观察对象实例（使用 `@Observable` ）。

### 4.1 基本用法

与 EnvironmentValue 类似， `@FocusedValue` 的使用需先声明 `FocusedValueKey` 并扩展 `FocusedValues` ：

    struct MyFocusKey: FocusedValueKey {
        typealias Value = String
    }

    extension FocusedValues {
        var myKey: String? {  // Optional
            get { self[MyFocusKey.self] }
            set { self[MyFocusKey.self] = newValue }
        }
    }

在失去焦点时，系统会重置 `@FocusedValue` ，因此在声明 `FocusedValueKey` 时，默认值为 nil（ 无需设置默认值
）。

在应用中， `@FocusedValue` 的使用方式与 `@FocusedObject` 类似：

    struct ContentView: View {
        @FocusedValue(\.myKey) var key
        var body: some View {
            VStack {
                Text(key ?? "nil")
                SubView()
            }
        }
    }

    struct SubView:View {
        @State var key = "Hello"
        var body: some View {
            TextField("text",text:$key)
                .focusedValue(\.myKey, key)
        }
    }

### 4.2 注意事项与使用技巧

- 大部分在 `@FocusedObject` 中提及的注意事项与技巧同样适用于 `@FocusedValue` 。
- 在声明 `FocusedValueKey` 和扩展 `FocusedValues` 时，确保使用的类型为 Optional。
- 截至 Xcode 15.2 版本，尽管 `focusedValue` 支持发送由 `@Observable` 创建的实例， `@FocusedValue` 仍无法正常观察相应实例。此外，目前也缺乏支持 Observable 实例的 `focusedSceneValue` 版本。预计这些问题将在未来版本中得到解决。

## 5\. @FocusedBinding

`@FocusedBinding` 属性包装器赋予开发者在聚焦值观察端修改 `FocusedValueKey`
数据的能力，提供了更多的灵活性和控制权。。

### 5.1 基本用法

`@FocusedBinding` 允许在界面中直接修改与焦点相关的绑定数据。以下代码示例展示了如何在文本输入框和按钮中（
数据提供端和数据观察端）修改与 `myKey` 相关的数据：

    struct ContentView: View {
        @FocusedBinding(\.myKey) var key
        var body: some View {
            VStack {
                Text(key ?? "nil")
                Button("Change Key"){
                    key = "\(Int.random(in: 0..<100))"
                }
                SubView()
            }
        }
    }


    struct SubView:View {
        @State var key = "Hello"
        var body: some View {
            TextField("text",text:$key)
                .focusedValue(\.myKey, $key) // Binding
        }
    }

    struct MyFocusKey: FocusedValueKey {
        typealias Value = Binding<String> // Binding
    }

    extension FocusedValues {
        var myKey: Binding<String>? { // Optional
            get { self[MyFocusKey.self] }
            set { self[MyFocusKey.self] = newValue }
        }
    }

### 5.2 注意事项

- **绑定类型声明：** 在 `FocusedValueKey` 中声明的类型应为 `Binding` 。
- **值类型数据专用：** `@FocusedBinding` 仅用于值类型数据。待 `@Observable` 的相关问题解决后，无需使用 `Binding` 便可在观察端直接修改其属性（ 与 `@FocusedObject` 一样 ）。
- **SwiftUI 生命周期兼容性** ：当前 `@FocusedBinding` 仅在使用 SwiftUI 生命周期的应用中有效。

## 总结

Swift 语言的属性包装器与 SwiftUI 诞生于同一年。SwiftUI
充分利用这一功能，为开发者提供了一系列属性包装器，极大地简化了开发过程。在这个系列的四篇文章中，我们详细梳理了截至 iOS 17 时期 SwiftUI
所提供的全部属性包装器，旨在帮助开发者更加高效和便捷地使用 SwiftUI。希望这些内容能对大家在使用 SwiftUI 时提供有价值的指导和帮助。
