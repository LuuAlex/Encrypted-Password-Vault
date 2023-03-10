//
//  PasswordViews.swift
//  Encrypted Password Vault
//
//  Created by Alex Luu on 2/22/23.
//

import SwiftUI

struct PasswordViews: View {
    @Binding var showPathViews: Bool
    @Binding var showPasswordViews: Bool
    @Binding var showDataViews: Bool
    
    @State private var password = ""
    
    var body: some View {
        VStack {
            Text("Data Location: " + (getPath() ?? ""))
            
            HStack {
                Text("Enter your password: ")
                TextField("", text: $password)
                    .textFieldStyle(RoundedBorderTextFieldStyle())
            }
            
            NextButton(showPathViews: $showPathViews,
                       showPasswordViews: $showPasswordViews,
                       showDataViews: $showDataViews,
                       hide: password.isEmpty,
                       password: $password)
            
        }
        .frame(maxWidth: .infinity, maxHeight: .infinity)
    }
}

struct PasswordViews_Previews: PreviewProvider {
    static var previews: some View {
        PasswordViews(showPathViews: TestValues.$testFalse, showPasswordViews: TestValues.$testTrue, showDataViews: TestValues.$testFalse)
    }
}
