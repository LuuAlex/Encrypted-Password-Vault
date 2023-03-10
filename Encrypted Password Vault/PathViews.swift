//
//  PathViews.swift
//  Encrypted Password Vault
//
//  Created by Alex Luu on 2/22/23.
//

import SwiftUI

struct PathViews: View {
    @Binding var showPathViews: Bool
    @Binding var showPasswordViews: Bool
    @Binding var showDataViews: Bool
    
    @State var placeholder = "Select Folder"
    @State var filename = ""

    var body: some View {
        VStack {
            
            HStack {
                Text("Password Data Folder Location: ")
                Button(placeholder) {
                    let panel = NSOpenPanel()
                    panel.allowsMultipleSelection = false
                    panel.canChooseDirectories = true
                    panel.canChooseFiles = false
                    if panel.runModal() == NSApplication.ModalResponse.OK  {
                        self.placeholder = panel.url?.lastPathComponent ?? "Select Folder"
                        self.filename = panel.url?.path ?? ""
                        setPath(path: self.filename) // TODO
                    }
                }
            }

            NextButton(showPathViews: $showPathViews,
                       showPasswordViews: $showPasswordViews,
                       showDataViews: $showDataViews,
                       hide: filename.isEmpty,
                       password: $filename)
                
        }
        .frame(maxWidth: .infinity, maxHeight: .infinity)
    }
}

struct PathViews_Previews: PreviewProvider {
    static var previews: some View {
        PathViews(showPathViews: TestValues.$testTrue, showPasswordViews: TestValues.$testFalse, showDataViews: TestValues.$testFalse)
    }
}
