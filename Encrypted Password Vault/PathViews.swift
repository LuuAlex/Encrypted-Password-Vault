//
//  PathViews.swift
//  Encrypted Password Vault
//
//  Created by Alex Luu on 2/22/23.
//

import SwiftUI

struct PathViews: View {
    @Binding var showDataFolderLocation: Bool
    @Binding var showPasswordCheck: Bool
    @Binding var showAuthScreen: Bool
    
    @State var placeholder = "Select Folder"
    @State var filename = ""

    var body: some View {
        VStack {
            
            HStack {
                let _ = print(initalize())
                Text("Password Data Folder Location: ")
                Button(placeholder) {
                    let panel = NSOpenPanel()
                    panel.allowsMultipleSelection = false
                    panel.canChooseDirectories = true
                    panel.canChooseFiles = false
                    if panel.runModal() == .OK {
                        self.placeholder = panel.url?.lastPathComponent ?? "Select Folder"
                        self.filename = panel.url?.path ?? ""
                        panel.close()
                    }
                    setPath(path: self.filename) // TODO
                }
            }

            NextButton(showDataFolderLocation: $showDataFolderLocation,
                       showPasswordCheck: $showPasswordCheck,
                       showAuthScreen: $showAuthScreen,
                       hide: filename.isEmpty,
                       passwordScreen: false,
                       password: "")
                
        }
        .frame(maxWidth: .infinity, maxHeight: .infinity)
    }
}

struct PathViews_Previews: PreviewProvider {
    static var previews: some View {
        PathViews(showDataFolderLocation: TestValues.$testTrue, showPasswordCheck: TestValues.$testFalse, showAuthScreen: TestValues.$testFalse)
    }
}
