在本文中，我们将继续了解 SwiftUI 中的属性包装器： `@AppStorage` 、 `@SceneStorage` 、 `@FocusState` 、 `@GestureState` 以及 `@ScaledMetric`
。这些属性包装器涵盖了数据持久化、交互响应、辅助功能、多窗口支持等多个方面, 为开发者提供了简洁实用的解决方案。

> 本文旨在提供对这些属性包装器的主要功能和使用注意事项的概述，而非详尽的使用指南。

- [ @State、@Binding、@StateObject、@ObservedObject、@EnvironmentObject、@Environment ](/zh/posts/exploring-key-property-wrappers-in-swiftui/)
- [ @FetchRequest、@SectionedFetchRequest、@Query、@Namespace、@Bindable ](/zh/posts/exploring-swiftui-property-wrappers-3/)
- [ @UIApplicationDelegateAdaptor, @AccessibilityFocusState, @FocusedObject, @FocusedValue, @FocusedBinding ](/zh/posts/exploring-swiftui-property-wrappers-4/)

## 1\. @AppStorage

在 SwiftUI 中， `@AppStorage`
作为一个属性包装器，主要用于数据的持久化。它使我们能够轻松地将少量数据存储在用户的默认设置（UserDefaults）中。此外，当这些数据变更时，相关联的视图会自动进行更新。

### 1.1 基本用法

以下是 `@AppStorage` 的基本使用示例：

    @AppStorage("isLogin") var isLogin: Bool = false

### 1.2 主要功能

- `@AppStorage` 主用于存储和检索在应用全局范围内使用的数据，例如用户的偏好设置、上次访问时间、访问次数等。
- 通过 UserDefaults， `@AppStorage` 实现了数据的持久存储，确保即便应用关闭后，数据依然得以保存。
- 当 UserDefaults 中的相应值发生更改时， `@AppStorage` 自动更新视图，确保数据与界面保持同步。

### 1.3 注意事项与使用技巧

- UserDefaults 的持久化不是原子级别的，存在数据丢失的风险。因此，不建议使用 `@AppStorage` 来保存关键数据，即那些数据丢失后可能影响应用正常运行的信息。

- 同样也不建议用 `@AppStorage` 来保存敏感数据。

- `@AppStorage` 作为 SwiftUI 对 UserDefaults 的包装，其默认仅支持有限的数据类型。常见的数据类型如日期和数组等默认不被支持。开发者可通过让不支持的数据类型遵循 RawRepresentable 协议，以实现对更多类型的存储。更多信息请参阅： [ @AppStorage 研究 ](/zh/posts/appstorage/) 。

- 应确保保存的数据是轻量级的。不应将较大尺寸的数据存储在 `@AppStorage` 中，否则可能会导致性能下降。

- 除了默认的 `standard` suite， `@AppStorage` 也支持开发者定义的 UserDefaults suite。以下代码展示了如何将数据保存在 App Group 对应的 suite 中：

  public extension UserDefaults {
  static let appGroup = UserDefaults(suiteName: "group.com.fatbobman.myApp")!
  }

  @AppStorage("isLogin",store: .appGroup) var isLogin: Bool = false

- 使用 `defaultAppStorage` 可以为视图设置默认的 UserDefaults suite，从而免去在每个 `@AppStorage` 中重复设置：

  ContentView()
  .defaultAppStorage(.appGroup)

  @AppStorage("isLogin") var isLogin: Bool = false // in ContentView, store in appGroup suit

- 在 `@AppStorage` 中设置的默认值仅适用于其本身，不适用于直接访问 UserDefaults 的方式：

  @AppStorage("count") var count = 100

  // in View
  print(count) // 100
  print(UserDefaults.standard.value(forKey: "count")) // nil

- 使用 UserDefaults 的 `register` 方法设置的默认值可以适用于 `@AppStorage` ：

  struct DefaultValue: View {
  @AppStorage("count") var count = 100
  var body: some View {
  Button("Count") {
  print(count) // 50
  }
  }
  }

  DefaultValue()
  .onAppear {
  UserDefaults.standard.register(defaults: ["count": 50])
  }

- `@AppStorage` 中的键值对的默认值以首次设置的为准：

  @AppStorage("count") var count = 100
  @AppStorage("count") var count1 = 300

  print(count) // 100

- 可以将多个 `@AppStorage` 实例放在遵循 ObservableObject 协议的类中，以便进行统一管理。更多信息请参阅： [ @AppStorage 研究 ](/zh/posts/appstorage/) ：

  class Settings:ObservableObject {
  @AppStorage("count") var count = 100
  @AppStorage("isLogin") var isLogin = false
  }

  @StateObject var settings = Settings()
  Toggle("Login", isOn: $settings.isLogin)

- 与 UserDefaults 类似， `@AppStorage` 的键（Key）是基于字符串的。为了保证一致性和避免在不同视图中由于拼写错误导致的问题，建议采用上统一管理的方式，或者统一定义键。这种做法不仅减少了错误的风险，还使代码更易于维护和理解。

  enum Keys {
  static let count = "count"
  static let isLogin = "isLogin"
  }

  @AppStorage(Keys.count) var count = 0

## 2\. @SceneStorage

`@SceneStorage` 是一个专为场景（Scene）中数据共享而设计的属性包装器，主要适用于支持多场景的设备，例如 iPadOS、macOS 和
visionOS。它能够在每个独立场景中保存特定数据，非常适合用于多窗口或标签页应用，以保持用户界面状态的一致性和持续性。

### 2.1 基本用法

    @SceneStorage("selectedTab") private var selectedTab: Int = 0

### 2.2 主要功能

`@SceneStorage` 主要用于在同一个应用的不同实例或窗口间共享轻量级数据，例如用户在标签页中的选择或滚动视图的位置。

### 2.3 注意事项与使用技巧

- `@SceneStorage` 支持的数据类型与 `@AppStorage` 相同，其类型扩展方法亦如此。

- 与 `@AppStorage` 不同， `@SceneStorage` 不支持统一管理注入方式。

- `@SceneStorage` 是一个专属于 SwiftUI 的独特概念，它并不对应任何已知的底层数据结构。因此， `@SceneStorage` 应仅在视图内部使用，不应在视图外部或视图模型中使用它。

- 每个场景（Scene）之间的 `@SceneStorage` 数据是独立保存的，不会在不同场景间共享。若需跨场景共享数据，应使用 `@AppStorage` 或在应用层面创建的模型。

- `@SceneStorage` 的工作原理与 `@State` 相似，后者用于保存视图的私有状态，而 `@SceneStorage` 用于保存场景的私有状态。在某种意义上， `@SceneStorage` 可被视为场景中视图间共享数据的便捷方式，免去了为每个场景单独注入模型的需求。有关场景的概念及如何为不同场景注入模型的更多信息，请参阅 [ 打造可适配多平台的 SwiftUI 应用 ](/zh/posts/building-multiple-platforms-swiftui-app/#%E6%95%B0%E6%8D%AE%E6%BA%90) 。

- 尽管 `@SceneStorage` 展现了一定的持久化特性，系统并不保证数据保存的具体时间和持久化条件。特别是当场景被显式销毁时（例如，在 iPadOS 上关闭应用的切换器快照，或在 macOS 上关闭应用窗口），相关数据可能会随之丢失。值得注意的是，在实际应用中，即便应用已经被显式销毁，有时重新启动应用后系统可能仍保留最后一个场景的数据。然而，鉴于这种行为的不确定性，不建议将 `@SceneStorage` 作为数据持久化的主要手段。

## 3\. FocusState

`@FocusState` 是 SwiftUI 中用于管理焦点状态的属性包装器。它允许开发者在 SwiftUI 视图中轻松地跟踪和修改焦点状态。

### 3.1 基本用法

基于布尔类型的使用示例：

    @FocusState private var isNameFocused: Bool
    TextField("name:",text:$name)
        .focused($isNameFocused)

基于枚举类型的使用示例：

    enum FocusedField:Hashable{
        case name,password
    }

    @FocusState var focus:FocusedField?
    TextField("name:",text:$name)
        .focused($focus, equals: .name)

> 更多详细的使用方法，可参阅 [ SwiftUI TextField 进阶 —— 事件、焦点、键盘 ](/zh/posts/textfield-
> event-focus-keyboard/) 。

### 3.2 主要功能

- `@FocusState` 主要用于管理和追踪用户界面中的焦点状态。
- 可以通过设置 `@FocusState` 让特定输入字段获取焦点
- 它可以用来感知哪个输入字段或视图元素（ 已进行焦点绑定）当前拥有焦点。
- 通过绑定到视图的某些部分，可以在特定元素获得或失去焦点时执行动作。

### 3.3 注意事项与使用技巧

- 目前，只有 `TextField` 和 `TextEdit` 支持通过代码修改 `@FocusState` 的值来获得或失去焦点。
- 通过 `searchable` 创建的搜索栏无法通过 `@FocusState` 设置或获取焦点状态，对此有需求的开发者可参考 Daniel Saidi 提供的 [ 解决方案 ](https://danielsaidi.com/blog/2023/12/20/quick-search-with-swiftui-searchable) 。
- 在 iOS 17 之前，设置默认焦点需要在 `onAppear` 中进行；iOS 17 及以后的版本允许使用 `defaultFocus` 设置默认焦点，此功能同样适用于 macOS 和 tvOS。
- 在 tvOS 中， `@FocusState` 可以用于判断哪个视图当前获得了焦点。
- 使用 `focusable` 可以使原本不可聚焦的视图变得可聚焦。对于这类视图，只能通过键盘让其获得焦点（无法通过修改 `@FocusState` 直接设置），但可以通过关联 `@FocusState` 来指示其当前获得了焦点。例如：

  struct FocusableDemo: View {
  @FocusState private var isFocused
  var body: some View {
  VStack {
  Rectangle()
  .fill(.red.gradient)
  .overlay(
  Text("\(isFocused ? "focused" : "")").font(.largeTitle)
  )
  .padding()
  .focusable() // 允许聚焦
  .focusEffectDisabled() // 取消默认样式
  .focused($isFocused) // 必须放在 focusable 之后

              Rectangle()
                  .fill(.blue.gradient)
                  .padding()
                  .focusable()
          }
          .padding(50)
      }

  }

- 在使用时应避免焦点绑定的不明确性。在同一视图中，每个焦点绑定应该是明确且唯一的。

## 4\. @GestureState

`@GestureState` 是 SwiftUI
中用于简化手势处理的属性包装器，主要用于临时存储与手势相关的状态。当手势活动结束时，这些状态会自动重置。

### 4.1 基本用法

以下是 `@GestureState` 的基本使用示例（在手势取消后， `isPressed` 会被重置为 `false` ）：

    struct ContentView: View {
        @GestureState var isPressed = false
        var body: some View {
            VStack {
                Rectangle()
                    .fill(.orange).frame(width: 200, height: 200)
                    .gesture(DragGesture(minimumDistance: 0).updating($isPressed) { _, state, _ in
                        state = true
                    })
                    .overlay(
                        Text(isPressed ? "Pressing" : "")
                    )
            }
        }
    }

与此等价的基于 `@State` 的方式：

    struct ContentView: View {
        @State var isPressed = false
        var body: some View {
            VStack {
                Rectangle()
                    .fill(.orange).frame(width: 200, height: 200)
                    .gesture(DragGesture(minimumDistance: 0).onChanged{ _ in
                        isPressed = true
                    }.onEnded{ _ in
                        isPressed = false
                    })
                    .overlay(
                        Text(isPressed ? "Pressing" : "")
                    )
            }
        }
    }

> 阅读 [ 在 SwiftUI 下定制手势 ](/zh/posts/swiftuigesture/) 一文，以了解更多有关 SwiftUI 手势的内容。

### 4.2 主要功能

- `@GestureState` 常用于存储临时的手势数据，如拖拽的位移、旋转的角度等。
- 它会自动管理状态的生命周期，当手势结束时，状态会重置到初始值。
- 使用 `@GestureState` 可以让手势处理代码更加简洁，且易于维护。

### 4.3 注意事项与使用技巧

- `@GestureState` 仅适用于临时的、与手势相关的状态。它不适合用于长期存储或在应用的多个部分之间共享状态。
- 可以通过 `@GestureState` 的构造方法为状态复位设置 `Transaction` ，或根据复位时的状态值设定 `Transaction` 。以下代码演示了只有当横向移动距离超过 200 时才会给复位操作添加动画。更多关于 `Transaction` 的信息，请参阅 [ 掌握 Transaction，实现 SwiftUI 动画的精准控制 ](/zh/posts/mastering-transaction/) 。

  struct ContentView: View {
  @GestureState(wrappedValue: CGSize.zero, reset: { value, transaction in
  if abs(value.width) > 200 {
  transaction.animation = .smooth
  }
  }) var offset
  var body: some View {
  VStack {
  Rectangle()
  .fill(.orange).frame(width: 200, height: 200)
  .offset(x: offset.width, y: offset.height)
  .gesture(DragGesture().updating($offset) { value, state, \_ in
  state = value.translation
  })
  }
  }
  }

- 在 SwiftUI 中，某些系统操作可能会打断 SwiftUI 手势的正常处理流程，导致 `onEnded` 闭包不被执行。使用 `@GestureState` 可以确保即使手势被系统打断，相关状态仍会恢复到初始值。例如，在以下基于 `@State` 的代码示例中，如果用户在拖动过程中执行了系统操作（例如，用另一只手下拉控制中心），会导致 `offset` 无法恢复。而在使用 `@GestureState` 的版本中，状态可以正确地恢复。

  struct ContentView: View {
  @State var offset = CGSize.zero
  var body: some View {
  VStack {
  Rectangle()
  .fill(.orange).frame(width: 200, height: 200)
  .offset(x: offset.width, y: offset.height)
  .gesture(DragGesture().onChanged {
  offset = $0.translation
  }.onEnded { \_ in
  offset = .zero
  })
  }
  }
  }

## 5\. @ScaledMetric

`@ScaledMetric` 是 SwiftUI
中用于处理基于用户设定的文本大小自动缩放度量值的属性包装器。它主要用于适配不同用户的辅助功能需求，特别是那些需要根据系统设置中的字体大小变化来调整布局和元素大小的情况。

### 5.1 基本用法

以下是 `@ScaledMetric` 的基本使用示例：

    struct ContentView: View {
        @ScaledMetric var size: CGFloat = 100

        var body: some View {
            Image(systemName: "person.fill")
                .frame(width: size, height: size)
        }
    }

> 更多具体用例，请参阅 [ 在 SwiftUI 中用 Text 实现图文混排
> ](/zh/posts/mixing_text_and_graphics_with_text_in_swiftui/#%E5%8A%A8%E6%80%81%E7%B1%BB%E5%9E%8B-%E8%87%AA%E5%8A%A8%E7%BC%A9%E6%94%BE%E5%AD%97%E4%BD%93)
> 。

### 5.2 主要功能

- `@ScaledMetric` 用于根据用户的辅助功能设置（如更大的文本大小）自动调整数值。
- 它能够确保应用界面在不同用户偏好下保持可用性和舒适性。
- `@ScaledMetric` 可以用于调整任何需要根据系统字体大小比例变化的尺寸，如图标大小、布局间距等。

### 5.3 注意事项与使用技巧

- `@ScaledMetric` 的 `relativeTo` 参数允许将数值与特定的文本风格尺寸变化曲线相关联，默认对应 `body` 风格。

  @ScaledMetric(relativeTo: .largeTitle) var height = 17

- 不同的文本风格对动态类型变化的响应曲线不尽相同，因此其对 `@ScaledMetric` 的影响也非线性。

- 使用 `@ScaledMetric` 时需注意，其影响的是尺寸大小而非布局结构。确保应用在不同缩放级别下保持合理的布局和功能性（ 如结合 [ ViewThatFits ](/zh/posts/mastering-viewthatfits/) 、AnyLayout、 [ GeometryReader ](/zh/posts/geometryreader-blessing-or-curse/) 等）。
- `@ScaledMetric` 适用于动态尺寸调整，但需谨慎使用，以避免过度调整导致布局失衡或可读性降低。
- 可以通过 `.dynamicTypeSize` 限制视图的动态类型尺寸变化范围，防止布局异常。

## 总结

每种属性包装器都有其独特的适用场景和注意事项。 `@AppStorage` 适用于全局数据的轻量级持久化; `@SceneStorage`
专注于场景间状态共享； `@FocusState` 简化了焦点管理； `@GestureState` 自动化手势状态的生命周期； `@ScaledMetric` 实现了尺寸的自动缩放。

正确使用这些属性包装器可以让 SwiftUI 代码更加简洁高效。与直接使用底层 API 相比, 属性包装器抽象了许多细节,
开发者可以更加关注业务逻辑。当然, 还需要谨记它们的使用限制, 避免滥用。

未来，我们会对其他尚未介绍的属性包装器进行更多的探讨。
