//
//  ChangeViews.swift
//  Encrypted Password Vault
//
//  Created by Alex Luu on 2/17/23.
//

import Foundation
import SwiftUI

struct FileLocation: View {
    
    @State var placeholder = "Select Folder"
    @State var filename = "<none>"
    @State var showFileChooser = true
    
    @Binding var showDataFolderLocation: Bool
    @Binding var showPasswordCheck: Bool

    var body: some View {
        VStack {

            HStack {
                Text("Password Data Folder Location: ")
                Button(placeholder) {
                    let panel = NSOpenPanel()
                    panel.allowsMultipleSelection = false
                    panel.canChooseDirectories = true
                    panel.canChooseFiles = false
                    if panel.runModal() == .OK {
                        self.placeholder = panel.url?.lastPathComponent ?? "<none>"
                        self.filename = panel.url?.path ?? "<none>"
                    }
                }
            }

            Button {
                showDataFolderLocation.toggle()
                showPasswordCheck = true
            } label: {
                Text("Next")
                   .foregroundColor(.white)
            }
            .background(.blue)
            .cornerRadius(8)
            .disabled(filename == "<none>")
                
        }
    .frame(maxWidth: .infinity, maxHeight: .infinity)
    }
    
}

struct PasswordLockView: View {
    
    @State private var path = "/Users/alexluu/Downloads"
    @State private var password = "123"
    
    var body: some View {
        VStack {
            HStack {
                Text("Enter your password: ")
                TextField("/Users/alexluu/Downloads", text: $path)
                    .textFieldStyle(RoundedBorderTextFieldStyle())
                TextField("123", text: $password)
                    .textFieldStyle(RoundedBorderTextFieldStyle())
                let _ = print(runCreateCSV(path: path, password: password))
                let _ = print(runWrite(path: path, password: password, newDataEntry: ["ufe","xsf","12"]))
                Text(String(runRead(path: path, password: password)[0].getPass()))
                
            }
        }
    }
    
}
