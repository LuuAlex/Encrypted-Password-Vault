//
//  PasswordViews.swift
//  Encrypted Password Vault
//
//  Created by Alex Luu on 2/22/23.
//

import SwiftUI

struct PasswordViews: View {
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

struct PasswordViews_Previews: PreviewProvider {
    static var previews: some View {
        PasswordViews(showDataFolderLocation: TestValues.$testFalse, showPasswordCheck: TestValues.$testTrue, showAuthScreen: TestValues.$testFalse)
    }
}
