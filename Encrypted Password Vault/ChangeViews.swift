//
//  ChangeViews.swift
//  Encrypted Password Vault
//
//  Created by Alex Luu on 2/17/23.
//

import Foundation
import SwiftUI

struct NextButton: View {
    
    @Binding var showDataFolderLocation: Bool
    @Binding var showPasswordCheck: Bool
    @Binding var showAuthScreen: Bool
    
    @State var hide: Bool
    @State var passwordScreen: Bool
    @State var password: String
    
    var body: some View {
        Button ("Next") {
            if passwordScreen {
                if checkHashedPassword(password: password) || !checkPasswordExists() {
                    showPasswordCheck.toggle()
                    showAuthScreen = true
                    setPassword(password: password)
                }
            } else {
                showDataFolderLocation.toggle()
                showPasswordCheck = true
            }
        }
        .buttonStyle(.borderedProminent)
        //.foregroundColor(.white)
        //.background(.blue)
        //.cornerRadius(6)
        .disabled(hide)
    }
    
}

struct FileLocation: View {
    
    @Binding var showDataFolderLocation: Bool
    @Binding var showPasswordCheck: Bool
    @Binding var showAuthScreen: Bool
    
    @State private var placeholder = "Select Folder"
    @State private var filename = ""

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
                        self.placeholder = panel.url?.lastPathComponent ?? "Select Folder"
                        self.filename = panel.url?.path ?? ""
                        setPath(path: self.filename)
                    }
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

struct PasswordLockView: View {
    
    @Binding var showDataFolderLocation: Bool
    @Binding var showPasswordCheck: Bool
    @Binding var showAuthScreen: Bool
    
    @State private var password = ""
    
    var body: some View {
        VStack {
            HStack {
                Text("Enter your password: ")
                TextField("", text: $password)
                    .textFieldStyle(RoundedBorderTextFieldStyle())
            }
            
            NextButton(showDataFolderLocation: $showDataFolderLocation,
                       showPasswordCheck: $showPasswordCheck,
                       showAuthScreen: $showAuthScreen,
                       hide: password.isEmpty,
                       passwordScreen: true,
                       password: password)
        }
        .frame(maxWidth: .infinity, maxHeight: .infinity)
    }
    
}
