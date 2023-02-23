//
//  ViewsUtils.swift
//  Encrypted Password Vault
//
//  Created by Alex Luu on 2/22/23.
//

import Foundation
import SwiftUI

struct TestValues {
    @State static var testTrue = true
    @State static var testFalse = false
    @State static var testPassword = 12
    @State static var testPath = "/Downloads"
}

struct NextButton: View {
    
    @Binding var showPathViews: Bool
    @Binding var showPasswordViews: Bool
    @Binding var showDataViews: Bool
    
    @State var path = getPath()
    @State var hide: Bool
    @State var password: String
    
    var body: some View {
        Button ("Next") {
            if showPasswordViews {
                if checkHashedPassword(password: password) {

                } else if !checkPasswordExists() {
                    setPassword(password: password)
                    runCreateCSV(path: path ?? "~/Downloads", password: password)
                }
                showPasswordViews.toggle()
                showDataViews = true
            } else {
                showPathViews.toggle()
                showPasswordViews = true
            }
        }
        .buttonStyle(.borderedProminent)
        //.foregroundColor(.white)
        .tint(.blue)
        //.cornerRadius(6)
        //.disabled(hide)
    }
    
}
